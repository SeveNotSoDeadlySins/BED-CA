from db.db import mysql_conn
import datetime


def seed_bookings():
    cursor = mysql_conn.cursor()
    print("Seeding bookings table")
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id int(11) FOREIGN KEY REFERENCES users(id),
            resource_id int(11) FOREIGN KEY REFERENCE resources(id),
            booking_date date,
            start_time time,
            end_time time,
            status enum('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
            created_at DATETIME,
            updated_at DATETIME
        )
    """)

    # Insert sample rows
    users = [
        ("Alice", "alice@example.com", "password123"),
        ("Bob", "bob@example.com", "secure456"),
        ("Jeff", "jeff@example.com", "pass15t3"),
    ]

    time = datetime.datetime.now()
    users_hashed_password = []

    for name,email,plain_pw in users:
        hashed = hash_password(plain_pw)
        users_hashed_password.append((name, email, hashed, time, time))

    cursor.executemany("""
        INSERT INTO users (name, email, password, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s)
    """, users_hashed_password)

    print(cursor.rowcount, "rows inserted")

    mysql_conn.commit()
    print("Users table seeded successfully!")
    cursor.close()

if __name__ == "__main__":
    seed_users()
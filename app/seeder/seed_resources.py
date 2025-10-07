from db.db import mysql_conn
import datetime


def seed_resources():
    cursor = mysql_conn.cursor()
    print("In the seeder file")
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            type VARCHAR(255),
            status enum('available', 'unavailable') DEFAULT 'available', 
            created_at DATETIME,
            updated_at DATETIME
        )
    """)

    # Insert sample rows
    resources = [
        ("Sam's Amazing restaurant", "restaurant", "available"),
        ("Tony's restaurant", "restaurant", "available"),
        ("Wendy's", "fast food restaurant", "available"),
    ]

    time = datetime.datetime.now()


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
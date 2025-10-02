from db.db import mysql_conn
import datetime
import bcrypt

def hash_password(plain_password: str, rounds: int = 12) -> str:
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt(rounds))
    
    return hashed.decode('utf-8')

def seed_users():
    cursor = mysql_conn.cursor()
    print("In the seeder file")
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(255),
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
from db.db import mysql_conn
import datetime

def seed_users():
    cursor = mysql_conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100),
            created_at DATETIME,
            updated_at DATETIME
        )
    """)

    # Insert sample rows
    users = [
        ("Alice", "alice@example.com", "password123", datetime.datetime.now(), datetime.datetime.now()),
        ("Bob", "bob@example.com", "secure456", datetime.datetime.now(), datetime.datetime.now()),
        ("Jeff", "jeff@example.com", "pass15t3", datetime.datetime.now(), datetime.datetime.now()),

    ]

    cursor.executemany("""
        INSERT INTO users (name, email, password, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s)
    """, users)

    mysql_conn.commit()
    print("Users table seeded successfully!")
    cursor.close()

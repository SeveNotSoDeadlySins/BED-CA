from fastapi import FastAPI
from db.db import mysql_conn, mongo_client
from db.db import mysql_conn, mongo_client, resource_details_collection


app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to my test api",
        "test_data": [
            {"id": 1, "name": "Test User"},
            {"id": 2, "name": "Another User"}
        ]
    }

@app.get("/all-users")
def all_users():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return {"users": users}

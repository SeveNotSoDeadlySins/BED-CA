import time
import mysql.connector
from pymongo import MongoClient
import os

for i in range(10):
    try:
        mysql_conn = mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"]
        )
        break
    except mysql.connector.Error:
        print("Waiting for MySQL...")
        time.sleep(3)

for i in range(10):
    try:
        mongo_client = MongoClient(os.environ["MONGO_URI"])
        mongo_client.admin.command('ping')
        break
    except Exception:
        print("Waiting for MongoDB...")
        time.sleep(3)


from fastapi import FastAPI

app = FastAPI()

# Root endpoint with test data
@app.get("/")
def read_root():
    return {
        "message": "Welcome to ReserveNow API",
        "test_data": [
            {"id": 1, "name": "Test User"},
            {"id": 2, "name": "Another User"}
        ]
    }

# Simple test endpoint
@app.get("/test")
def test_endpoint():
    return {"status": "FastAPI is working!"}

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to ReserveNow API"}

# @app.get("/all-users")
# def all_users():
#     cursor = mysql_conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     return {"users": users}


# # --- Display all MySQL resources ---
# @app.get("/all-resources")
# def all_resources():
#     cursor = mysql_conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM resources")
#     resources = cursor.fetchall()
#     cursor.close()
#     return {"resources": resources}


# # --- Display all MongoDB resource details ---
# @app.get("/all-resource-details")
# def all_resource_details():
#     details = list(resource_details_collection.find({}, {"_id": 0}))
#     return {"resource_details": details}


# # --- Display combined MySQL + MongoDB for a resource ---
# @app.get("/resource/{resource_id}")
# def resource(resource_id: int):
#     # MySQL core resource
#     cursor = mysql_conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM resources WHERE id = %s", (resource_id,))
#     resource = cursor.fetchone()
#     cursor.close()

#     # MongoDB extra details
#     details = resource_details_collection.find_one({"mysql_resource_id": resource_id}, {"_id": 0})

#     return {"core": resource, "details": details}
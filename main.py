from fastapi import FastAPI
import mysql.connector
from pymongo import MongoClient

app = FastAPI()

# ---- MySQL Connection ----
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bed-ca-1"
)

# ---- MongoDB Connection ----
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["BED-CA-1"]
resource_details_collection = mongo_db["resource_details"]

@app.get("/")
def read_root():
    return {"message": "Welcome to ReserveNow API"}

@app.get("/all-users")
def all_users():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return {"users": users}


# --- Display all MySQL resources ---
@app.get("/all-resources")
def all_resources():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM resources")
    resources = cursor.fetchall()
    cursor.close()
    return {"resources": resources}


# --- Display all MongoDB resource details ---
@app.get("/all-resource-details")
def all_resource_details():
    details = list(resource_details_collection.find({}, {"_id": 0}))
    return {"resource_details": details}


# --- Display combined MySQL + MongoDB for a resource ---
@app.get("/resource/{resource_id}")
def resource(resource_id: int):
    # MySQL core resource
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM resources WHERE id = %s", (resource_id,))
    resource = cursor.fetchone()
    cursor.close()

    # MongoDB extra details
    details = resource_details_collection.find_one({"mysql_resource_id": resource_id}, {"_id": 0})

    return {"core": resource, "details": details}
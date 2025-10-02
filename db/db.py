import time
import os
import mysql.connector
from pymongo import MongoClient

# --- MySQL Connection ---
mysql_conn = None
for i in range(10):
    try:
        mysql_conn = mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"]
        )
        print("Connecting to MySQL at", os.environ.get("MYSQL_HOST"), "DB:", os.environ.get("MYSQL_DATABASE"))

        break
    except mysql.connector.Error as e:
        print("Waiting for MySQL}")
        time.sleep(3)

# --- MongoDB Connection ---
mongo_client = None
for i in range(10):
    try:
        mongo_client = MongoClient(os.environ["MONGO_URI"])
        mongo_client.admin.command("ping")
        print("Connected to MongoDB")
        break
    except Exception as e:
        print("Waiting for MongoDB")
        time.sleep(3)
        
resource_details_collection = mongo_client["bed-ca-1"]["resource_details"]


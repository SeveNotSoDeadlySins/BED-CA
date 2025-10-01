import time
import mysql.connector
from pymongo import MongoClient
import os

# MYSQL
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

# Mongo DB
for i in range(10):
    try:
        mongo_client = MongoClient(os.environ["MONGO_URI"])
        mongo_client.admin.command('ping')
        break
    except Exception:
        print("Waiting for MongoDB...")
        time.sleep(3)
from fastapi import FastAPI
from app.db.db import mysql_conn, mongo_client
from app.routers.router import router

app = FastAPI(title='Placeholder title')

app.include_router(router)

@app.get("/")
def read_root():
    return {'message': "Welcome to reserve now"}


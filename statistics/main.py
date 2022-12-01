from fastapi import FastAPI

from statistics.db import initialize_db

app = FastAPI()
db = initialize_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

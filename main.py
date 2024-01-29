from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime 
import uvicorn
from os import environ
from Db import get_students, get_notes


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/compute-all-students-grades")
def read_student(dateA: datetime, dateB: datetime):
    return {"message": "Hello World"}


if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from Student import Student 
from Note import Note 
import uvicorn
from os import environ

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Students Database
students_db = [
    Student(id=17072, name="Angel Macias"),
    Student(id=17075, name="Daniel Cardenas"),
    Student(id=17078, name="Nico Herbas"),
    Student(id=17081, name="Galo Hernandez"),
    # You can add more students as needed
]

# Notes Database
notes_db = [
    Note(student_id=17072, grade=8, date=datetime(2023, 1, 15)),
    Note(student_id=17072, grade=9, date=datetime(2023, 2, 20)),
    Note(student_id=17075, grade=92.0, date=datetime(2023, 3, 5)),
    Note(student_id=17075, grade=85.5, date=datetime(2023, 4, 10)),
    Note(student_id=17078, grade=78.0, date=datetime(2023, 5, 15)),
    Note(student_id=17078, grade=88.5, date=datetime(2023, 6, 20)),
    Note(student_id=17081, grade=95.0, date=datetime(2023, 7, 5)),
    Note(student_id=17081, grade=90.5, date=datetime(2023, 8, 10)),
    # You can add more notes with dates in 2023 as needed
]

@app.get("/compute-all-students-grades")
def read_student(dateA: datetime, dateB: datetime):
    return {"message": "Hello World"}


if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List
import uvicorn

from os import environ
from Db import get_students, get_notes
from period import Period


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/compute")
def read_student(request: List[Period]):
    p1 = request[0]
    p2 = request[1]

    if p1.dateA > p1.dateB:
        raise HTTPException(status_code=400, detail="Invalid dateA")
    if p1.dateB > p2.dateA:
        raise HTTPException(status_code=400, detail="Invalid dateB")
    if p2.dateA > p2.dateB:
        raise HTTPException(status_code=400, detail="Invalid dateC")
    
    notes = get_notes()
    students = get_students()

    # get all the notes for each period for each student
    notes_p1 = []
    notes_p2 = []

    for note in notes:
        if p1.dateA <= note.date <= p1.dateB:
            notes_p1.append(note)
        elif p2.dateA <= note.date <= p2.dateB:
            notes_p2.append(note)
    
    # get the average for each student
    average_p1 = {}
    average_p2 = {}

    for note in notes_p1:
        if note.student_id in average_p1:
            average_p1[note.student_id].append(note.grade)
        else:
            average_p1[note.student_id] = [note.grade]

    for note in notes_p2:
        if note.student_id in average_p2:
            average_p2[note.student_id].append(note.grade)
        else:
            average_p2[note.student_id] = [note.grade]
    
    for student in students:
        if student.id not in average_p1:
            average_p1[student.id] = []
        if student.id not in average_p2:
            average_p2[student.id] = []

    # compute the average for each student
    for student_id, grades in average_p1.items():
        average_p1[student_id] = sum(grades) / len(grades)

    for student_id, grades in average_p2.items():
        average_p2[student_id] = sum(grades) / len(grades)
    
    # compute the final grade for each student
    final_grades = {}

    for student_id in average_p1:
        final_grades[student_id] = average_p1[student_id] * p1.weight + average_p2[student_id] * p2.weight

    return final_grades


if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

from datetime import datetime
from fastapi import HTTPException
from note import Note
from period import Period
from typing import List
from student import Student

students_db = [
    Student(id=17072, name="Paula Polisinlinker"),
    Student(id=17075, name="Daniel Cardenas"),
    Student(id=17078, name="Nico Herbas"),
    Student(id=17081, name="Galo Hernandez"),
    Student(id=17290, name="Poli Linker"),
]

# Notes Database
notes_db = [
    Note(student_id=17072, grade=10, date=datetime(2024, 1, 15)),
    Note(student_id=17072, grade=10, date=datetime(2024, 2, 20)),
    Note(student_id=17072, grade=10, date=datetime(2024, 3, 5)),
    Note(student_id=17072, grade=10, date=datetime(2024, 4, 10)),
    Note(student_id=17072, grade=10, date=datetime(2024, 5, 15)),
    Note(student_id=17072, grade=10, date=datetime(2024, 6, 20)),
    Note(student_id=17072, grade=9, date=datetime(2024, 7, 5)),
    Note(student_id=17072, grade=10, date=datetime(2024, 8, 10)),
    Note(student_id=17072, grade=10, date=datetime(2024, 9, 15)),
    Note(student_id=17072, grade=10, date=datetime(2024, 10, 20)),
    Note(student_id=17072, grade=9, date=datetime(2024, 11, 5)),
    Note(student_id=17072, grade=10, date=datetime(2024, 12, 10)),

    Note(student_id=17075, grade=5, date=datetime(2024, 1, 5)),
    Note(student_id=17075, grade=6, date=datetime(2024, 2, 10)),
    Note(student_id=17075, grade=9, date=datetime(2024, 3, 15)),
    Note(student_id=17075, grade=7, date=datetime(2024, 4, 20)),
    Note(student_id=17075, grade=8, date=datetime(2024, 5, 5)),
    Note(student_id=17075, grade=1, date=datetime(2024, 6, 10)),
    Note(student_id=17075, grade=9, date=datetime(2024, 7, 15)),
    Note(student_id=17075, grade=8, date=datetime(2024, 8, 20)),
    Note(student_id=17075, grade=9, date=datetime(2024, 9, 5)),
    Note(student_id=17075, grade=6, date=datetime(2024, 10, 10)),
    Note(student_id=17075, grade=8, date=datetime(2024, 11, 15)),
    Note(student_id=17075, grade=9, date=datetime(2024, 12, 20)),

    Note(student_id=17078, grade=7, date=datetime(2024, 1, 15)),
    Note(student_id=17078, grade=4, date=datetime(2024, 2, 20)),
    Note(student_id=17078, grade=8, date=datetime(2024, 3, 25)),
    Note(student_id=17078, grade=9, date=datetime(2024, 4, 5)),
    Note(student_id=17078, grade=5, date=datetime(2023, 5, 10)),
    Note(student_id=17078, grade=7, date=datetime(2024, 6, 15)),
    Note(student_id=17078, grade=4, date=datetime(2024, 7, 20)),
    Note(student_id=17078, grade=8, date=datetime(2024, 8, 25)),
    Note(student_id=17078, grade=4, date=datetime(2024, 9, 5)),
    Note(student_id=17078, grade=5, date=datetime(2024, 10, 10)),
    Note(student_id=17078, grade=7, date=datetime(2024, 11, 15)),
    Note(student_id=17078, grade=4, date=datetime(2024, 12, 20)),

    Note(student_id=17081, grade=9, date=datetime(2024, 1, 5)),
    Note(student_id=17081, grade=1, date=datetime(2024, 2, 10)),
    Note(student_id=17081, grade=7, date=datetime(2024, 3, 15)),
    Note(student_id=17081, grade=9, date=datetime(2024, 4, 20)),
    Note(student_id=17081, grade=5, date=datetime(2024, 5, 25)),
    Note(student_id=17081, grade=7, date=datetime(2024, 6, 5)),
    Note(student_id=17081, grade=6, date=datetime(2024, 7, 10)),
    Note(student_id=17081, grade=5, date=datetime(2024, 8, 15)),
    Note(student_id=17081, grade=7, date=datetime(2024, 9, 20)),
    Note(student_id=17081, grade=9, date=datetime(2024, 10, 25)),
    Note(student_id=17081, grade=5, date=datetime(2024, 11, 5)),
    Note(student_id=17081, grade=10, date=datetime(2024, 12, 10)),

    Note(student_id=17290, grade=10, date=datetime(2024, 1, 15)),
    Note(student_id=17290, grade=10, date=datetime(2024, 2, 20)),
    Note(student_id=17290, grade=10, date=datetime(2024, 3, 25)),
    Note(student_id=17290, grade=10, date=datetime(2024, 4, 5)),
    Note(student_id=17290, grade=10, date=datetime(2024, 5, 10)),
    Note(student_id=17290, grade=10, date=datetime(2024, 6, 15)),
    Note(student_id=17290, grade=10, date=datetime(2024, 7, 20)),
    Note(student_id=17290, grade=10, date=datetime(2024, 8, 25)),
    Note(student_id=17290, grade=10, date=datetime(2024, 9, 5)),
    Note(student_id=17290, grade=10, date=datetime(2024, 10, 10)),
    Note(student_id=17290, grade=10, date=datetime(2024, 11, 15)),
    Note(student_id=17290, grade=10, date=datetime(2024, 12, 20)),
]

def get_student(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    return None

def compute_grades(periods: List[Period]):
    try:
        p1, p2 = periods

        if p1.dateA > p1.dateB or p1.dateB > p2.dateA or p2.dateA > p2.dateB:
            raise HTTPException(status_code=400, detail="Invalid date range")

        if p1.weight + p2.weight >= 1 or p1.weight < 0 or p2.weight < 0:
            raise HTTPException(status_code=400, detail="Invalid weights")
        
        notes = notes_db
        students = students_db

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

        if len(notes_p1) == 0 or len(notes_p2) == 0:
            raise HTTPException(status_code=400, detail="No notes in the specified range")

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

            grade = average_p1[student_id] * p1.weight + average_p2[student_id] * p2.weight,

            final_grades[student_id] = {
                "name": get_student(student_id).name ,
                "grade": grade,

                "p1": average_p1[student_id],
                "p2": average_p2[student_id],

                "p1_weight": p1.weight,
                "p2_weight": p2.weight,

                "needed": 6 - grade[0] if grade[0] < 6 else 0,
            }

        return final_grades
    except:
        raise HTTPException(status_code=400, detail=f"Invalid request,{periods}")
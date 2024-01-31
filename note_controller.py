from fastapi import HTTPException
from period import Period
from datetime import datetime
from typing import List
from database import get_notes, get_students, get_student

def compute_grades(periods: List[Period]):
    try:
        p1, p2 = periods

        if p1.dateA > p1.dateB or p1.dateB > p2.dateA or p2.dateA > p2.dateB:
            raise HTTPException(status_code=400, detail="Invalid date range")

        if p1.weight + p2.weight >= 1 or p1.weight < 0 or p2.weight < 0:
            raise HTTPException(status_code=400, detail="Invalid weights")
        
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
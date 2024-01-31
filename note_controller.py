from fastapi import HTTPException
from period import Period
from datetime import datetime
from typing import List
from db import get_students, get_notes, get_student

def get_grades(p1: Period , p2: Period):
    try:
        p1 = Period(
            dateA=p1.dateA.date() if isinstance(p1.dateA, datetime) else datetime.strptime(p1.dateA.split("T")[0], "%Y-%m-%d").date(), 
            dateB=p1.dateB.date() if isinstance(p1.dateB, datetime) else datetime.strptime(p1.dateB.split("T")[0], "%Y-%m-%d").date(), 
            weight=p1.weight
        )
        p2 = Period(
            dateA=p2.dateA.date() if isinstance(p2.dateA, datetime) else datetime.strptime(p2.dateA.split("T")[0], "%Y-%m-%d").date(), 
            dateB=p2.dateB.date() if isinstance(p2.dateB, datetime) else datetime.strptime(p2.dateB.split("T")[0], "%Y-%m-%d").date(), 
            weight=p2.weight
        )

        if p1.dateA > p1.dateB:
            raise HTTPException(status_code=400, detail="Invalid dateA")
        if p1.dateB > p2.dateA:
            raise HTTPException(status_code=400, detail="Invalid dateB")
        if p2.dateA > p2.dateB:
            raise HTTPException(status_code=400, detail="Invalid dateC")
        
        if p1.weight + p2.weight >= 1:
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
            final_grades[student_id] = [ get_student(student_id).name ,average_p1[student_id] * p1.weight + average_p2[student_id] * p2.weight]

        return final_grades
    except:
        raise HTTPException(status_code=400, detail="Invalid request")
    
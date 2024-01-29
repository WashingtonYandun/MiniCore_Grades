from Student import Student 
from Note import Note
from datetime import datetime


# Students Database
students_db = [
    Student(id=17072, name="Angel Macias"),
    Student(id=17075, name="Daniel Cardenas"),
    Student(id=17078, name="Nico Herbas"),
    Student(id=17081, name="Galo Hernandez"),
]

# Notes Database
notes_db = [
    Note(student_id=17072, grade=8, date=datetime(2023, 1, 15)),
    Note(student_id=17072, grade=7, date=datetime(2023, 2, 20)),
    Note(student_id=17075, grade=10, date=datetime(2023, 2, 5)),
    Note(student_id=17075, grade=8, date=datetime(2023, 2, 10)),
    Note(student_id=17078, grade=7, date=datetime(2023, 3, 15)),
    Note(student_id=17078, grade=4, date=datetime(2023, 3, 20)),
    Note(student_id=17081, grade=9, date=datetime(2023, 4, 5)),
    Note(student_id=17081, grade=5, date=datetime(2023, 4, 10)),
]


def get_students():
    """
    Returns the list of students in the database.
    """
    return students_db


def get_notes():
    """
    Returns the list of notes in the database.
    """
    return notes_db

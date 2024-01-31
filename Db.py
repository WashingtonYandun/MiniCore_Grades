from student import Student 
from note import Note
from datetime import datetime


# Students Database
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


def get_student(id: int):
    """
    Returns the student with the given ID.
    """
    for student in students_db:
        if student.id == id:
            return student
    return None
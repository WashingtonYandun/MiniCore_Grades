from pydantic import BaseModel, confloat
from datetime import datetime


class Note(BaseModel):
    """
    Represents a note for a student's grade.

    Attributes:
        student_id (int): The ID of the student.
        grade (float): The grade received by the student.
        date (datetime): The date when the grade was recorded.
    """
    student_id: int
    grade: confloat(ge=0, le=10)
    date: datetime
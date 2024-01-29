from pydantic import BaseModel
from datetime import datetime, timedelta

class Student(BaseModel):
    """
    Represents a student.

    Attributes:
        id (int): The unique identifier of the student.
        name (str): The name of the student.
    """
    id: int
    name: str
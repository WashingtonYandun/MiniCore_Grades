from pydantic import BaseModel
from datetime import datetime, timedelta

class Note(BaseModel):
    student_id: int
    grade: float
    date: datetime
from pydantic import BaseModel
from datetime import datetime, timedelta

class Student(BaseModel):
    id: int
    name: str
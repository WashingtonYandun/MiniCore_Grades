from pydantic import BaseModel, confloat
from datetime import datetime


class Period(BaseModel):
    """
    Represents a period of time with start and end dates.

    Attributes:
        dateA (datetime): The start date of the period.
        dateB (datetime): The end date of the period.
        weight (float): The weight of the period, ranging from 0 to 1.
    """
    dateA: datetime
    dateB: datetime
    weight: confloat(ge=0, le=1)


class PeriodRequest(BaseModel):
    """
    Represents a period request.

    Attributes:
        dateA (str): The start date of the period.
        dateB (str): The end date of the period.
        weight (float): The weight of the period.
    """
    dateA: str
    dateB: str
    weight: float

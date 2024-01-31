from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import uvicorn
from os import environ
from period import Period, PeriodRequest
from note_controller import compute_grades
from database import get_students


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/compute")
def read_student(request: List[PeriodRequest]):
    try:
        

        periods = []

        for period_data in request:
            date_a = datetime.strptime(period_data.dateA, "%Y-%m-%d")
            date_b = datetime.strptime(period_data.dateB, "%Y-%m-%d")

            period = Period(dateA=date_a, dateB=date_b, weight=period_data.weight)
            periods.append(period)

        res = compute_grades(periods)

        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/students")
def read_students():
    return get_students()


if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

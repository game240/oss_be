from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

info_router = APIRouter()

class Info(BaseModel):
    student_id: str
    name: str
    courses: List[Dict[str, object]]

grade_map = {
    "A+": 4.5,
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "B0": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "C0": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "D0": 1.0,
    "F": 0.0,
}

@info_router.post("/info")
async def get_student_info(info: Info) -> dict:
    total_credits = 0
    total_grade = 0.0

    for course in info.courses:
        #    "course_code": "I040-2-4141",
        #    "course_name": "정보디자인프로그래밍실습",
        #    "credits": 3,
        #    "grade": "A+"
        grade = course.get("grade", "F")

        point = grade_map[grade]
        credits = course.get("credits", 0)

        total_credits += credits
        total_grade += credits * point

    # 그냥 하면 4.12, epsilon 추가
    epsilon = 10 ** -8
    gpa = round((total_grade / total_credits) + epsilon, 2)

    return {
        "student_summary": {
            "student_id": info.student_id,
            "name": info.name,
            "gpa": gpa,
            "total_credits": total_credits
        }
    }

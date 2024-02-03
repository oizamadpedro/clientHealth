from pydantic import BaseModel
from enum import Enum

class Gender(Enum):
    M = 'M'
    F = 'F'

class Client(BaseModel):
    name: str
    birthday_date: str
    gender: Gender
    health_problem_name: str
    health_problem_grade: str
    created_at: str
    updated_at: str
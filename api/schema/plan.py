from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class PlanBase(BaseModel):
    userid: int
    start: date
    end: date
    serve: int = 1
    recipes: Optional[List]


class PlanCreate(PlanBase):
    pass


class Plan(PlanBase):
    id: int

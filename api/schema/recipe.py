from typing import List
from pydantic import BaseModel


class RecipeBase(BaseModel):
    ingredients: List[dict]
    nutrition: List[dict]
    preptime: int
    difficulty: str
    name: str
    notincluded: str
    instruction: List[str]

    class Config:
        orm_mode = True


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int

from typing import List, Optional
from pydantic import BaseModel


class RecipeBase(BaseModel):
    ingredients: dict
    nutrition: dict
    preptime: int
    difficulty: str
    name: str
    notincluded: Optional[List[str]]
    instruction: Optional[List[str]]

    class Config:
        orm_mode = True


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int

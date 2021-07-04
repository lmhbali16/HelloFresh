from schema.recipe import Recipe, RecipeCreate
from fastapi import APIRouter
from fastapi import Depends
from starlette.status import HTTP_200_OK
from .token import verifyToken
from postgres.database import SessionLocal
from postgres.crud.recipeCrud import (
                                        createRecipe, deleteRecipe,
                                        getRecipes, getRecipeByName,
                                        updateRecipe)


recipeRouter = APIRouter(prefix='/recipe', dependencies=[Depends(verifyToken)])


@recipeRouter.get('/')
def mainRecipe():
    return getRecipes(SessionLocal())


@recipeRouter.get('/get')
def retrieveRecipe(name: str):
    return getRecipeByName(SessionLocal(), name)


@recipeRouter.post('/delete')
def removeRecipe(id: int):
    deleteRecipe(SessionLocal(), id)

    return HTTP_200_OK


@recipeRouter.post('/update')
def changeRecipe(recipe: Recipe):
    updateRecipe(SessionLocal(), recipe)


@recipeRouter.post('/create')
def addRecipe(recipe: RecipeCreate):
    createRecipe(SessionLocal(), recipe)

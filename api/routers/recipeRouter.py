from schema.recipe import Recipe, RecipeCreate
from fastapi import APIRouter
from fastapi import Depends
from starlette.status import HTTP_200_OK
from .token import verifyToken
from postgres.database import SessionLocal
from postgres.crud.recipeCrud import (
                                        createRecipe, deleteRecipe,
                                        getRecipes, getRecipe,
                                        updateRecipe)


recipeRouter = APIRouter(prefix='/recipe', dependencies=[Depends(verifyToken)])


@recipeRouter.get('/')
def mainRecipe():
    return getRecipes(SessionLocal())


@recipeRouter.get('/get')
def retrieveRecipe(id: int):
    return getRecipe(SessionLocal(), id)


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

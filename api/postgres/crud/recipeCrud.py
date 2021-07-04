from sqlalchemy.orm import Session
from postgres.models import Recipe
from schema.recipe import Recipe as RecipeAPI
from schema.recipe import RecipeCreate
from sqlalchemy.sql.expression import update
from postgres.models import Plan


def getRecipe(session: Session, id: int):
    '''
    Get a recipe by ID

    Parameters:
        session (Session): db session
        id (int): ID of the recipe

    Returns:
        Recipe: Recipe object from postgres.models

    '''
    return session.query(Recipe).filter(Recipe.id == id).first()


def updateRecipe(session: Session, recipe: RecipeAPI):
    '''
    Update a recipe

    Parameters:
        session (Session): db session
        recipe (RecipeAPI): a schema.recipe.Recipe object

    Returns:
        None: no return value
    '''

    smt = update(Recipe).where(Recipe.id == recipe.id).values(**recipe.dict())
    session.execute(smt)


def deleteRecipeFromPlan(session: Session, planID: int, id: int):
    '''
    Remove a recipe from a plan

    Parameters:
        session (Session): db session
        planID (int): plan ID
        id (int): recipe ID

    Returns:
        None: no return value

    '''

    plan = session.query(Plan).filter(Plan.id == planID).first()
    recipe = getRecipe(session, id)
    plan.recipes.remove(recipe)
    session.add(plan)
    session.commit()


def addRecipeToPlan(session: Session, planID: int, id: int):
    '''
    Add a recipe to the plan

    Parameters:
        session (Session): db session
        planID (int): planID
        id (int): recipe ID

    Returns:
        None: no return value

    '''

    plan = session.query(Plan).filter(Plan.id == planID).first()
    recipe = getRecipe(session, id)
    plan.recipes.append(recipe)
    session.add(plan)
    session.commit()


def createRecipe(session: Session, recipe: RecipeCreate):
    '''
    Create a new recipe

    Parameters:
        session (Session): db session
        recipe (RecipeCreate): a RecipeCreate object

    Returns:
        None: No return value

    '''

    recipeDB = Recipe(**recipe.dict())
    session.add(recipeDB)
    session.commit()


def deleteRecipe(session: Session, id: int):
    '''
    Delete a recipe by ID

    Parameters:
        session (Session): db session
        id (int): recipe ID

    Returns:
        None: no return value

    '''
    recipe = getRecipe(session, id)
    session.delete(recipe)
    session.commit()


def getRecipeByName(session: Session, name: str):
    '''
    Get a recipe by name

    Parameters:
        session (Session): db session
        name (str): name of the recipe

    Returns:
        Recipe: Recipe object from postgres.models

    '''
    return session.query(Recipe).filter(Recipe.name == name).first()


def deleteRecipeByName(session: Session, name: str):
    '''
    Delete a recipe by name

    Parameters:
        session (Session): db session
        name (str): recipe name

    Returns:
        None: no return value

    '''
    recipe = getRecipeByName(session, name)
    session.delete(recipe)
    session.commit()


def getRecipes(session: Session):
    '''
    Get all the recipes

    Parameters:
        session (Session): db session

    Returns:
        list: list of recipes Recipe ORM

    '''
    return session.query(Recipe).all()

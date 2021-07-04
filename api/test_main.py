from postgres.crud.recipeCrud import createRecipe, getRecipes
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from postgres.crud.userCrud import (
                                    createUser, getUser,
                                    getUserByEmail, updateUser)
from test.test_helper import get_recipe, get_user
from postgres.models import Recipe, Users

load_dotenv('.env')
username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}'\
                            '@localhost:5432/postgres'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(
                            autocommit=False,
                            expire_on_commit=False,
                            autoflush=False,
                            bind=engine)
db = SessionLocal(expire_on_commit=False)


@pytest.fixture
def create_user():
    user = get_user()
    userDB = Users(**user.dict())
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    yield

    db.delete(userDB)
    db.commit()


@pytest.fixture
def delete_user():
    yield

    user = db.query(Users).filter(Users.email == 'hello@fresh.com').first()
    db.delete(user)
    db.commit()


@pytest.fixture
def delete_recipe():
    yield
    recipe = get_recipe()
    recipe = db.query(Recipe).filter(Recipe.name == recipe.name).first()
    db.delete(recipe)
    db.commit()


@pytest.fixture
def create_recipe():
    recipe = get_recipe()
    recipeDB = Recipe(**recipe.dict())
    db.add(recipeDB)
    db.commit()
    db.refresh(recipeDB)
    yield
    db.delete(recipeDB)
    db.commit()


def test_create_user(delete_user):
    '''
    Test creating user
    '''
    user = get_user()

    createUser(db, user)

    user = db.query(Users).filter(Users.email == 'hello@fresh.com').first()

    assert user.name == 'hellofresh'


def test_get_user(delete_user):
    '''
    Test getting a User
    '''
    user = get_user()
    userDB = Users(**user.dict())
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    check_user = getUser(db, userDB.id)

    assert check_user.email == 'hello@fresh.com'


def test_get_user_by_email(create_user):
    '''
    Test getting a user by email
    '''
    user = getUserByEmail(db, 'hello@fresh.com')
    assert user.name == 'hellofresh'


def test_update_user(delete_user):
    '''
    Test updating a user
    '''
    user = get_user()
    userDB = Users(**user.dict())
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    updateUser(db, userDB.id, {'name': 'Hoang'})
    check_user = db.query(Users).filter(Users.name == 'Hoang').first()
    assert check_user.email == 'hello@fresh.com'
    updateUser(db, userDB.id, {'name': 'hellofresh'})


def test_create_recipe(delete_recipe):
    recipe = get_recipe()

    createRecipe(db, recipe)
    recipeDB = db.query(Recipe).filter(Recipe.name == recipe.name).first()

    assert recipeDB.name == recipe.name


def test_get_all_recipes(create_recipe):
    list_recipes = getRecipes(db)
    recipe = get_recipe()
    assert len(list_recipes) == 1
    assert list_recipes[0].name == recipe.name

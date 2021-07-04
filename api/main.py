from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from postgres import models
from postgres.crud.userCrud import createUser, getUserByEmail, updateUser
from schema.user import UserCreate
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from postgres.database import SessionLocal, engine
from routers.token import getAccessToken
from routers.recipeRouter import recipeRouter
from routers.planRouter import planRouter


models.Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/api/a/docs', openapi_url='/api/a/openapi.json')
app.include_router(recipeRouter)
app.include_router(planRouter)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def main():

    return {'hello': 'world'}


@app.post('/signup')
def signUp(user: UserCreate, db: Session = Depends(get_db)):
    email = user.email
    existing_user = getUserByEmail(db, email)
    if existing_user is not None:
        raise HTTPException(
                            status_code=HTTP_400_BAD_REQUEST,
                            detail='Email exist')

    createUser(db, user)

    return HTTP_200_OK


@app.post('/login')
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = getUserByEmail(db, email)

    if user is None:
        raise HTTPException(
                            status_code=HTTP_400_BAD_REQUEST,
                            detail='No user with this email')

    if user.password != password:
        raise HTTPException(
                            status_code=HTTP_400_BAD_REQUEST,
                            detail='Incorrect password')

    updateUser(db, user.id, {'login': True})
    return getAccessToken(email, password)

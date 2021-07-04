from fastapi import Header
from postgres.crud.userCrud import getUserByEmail
from dotenv import load_dotenv
from fastapi import HTTPException
import jwt
from jwt import DecodeError, ExpiredSignatureError
import os
from postgres.database import SessionLocal
from starlette.status import HTTP_401_UNAUTHORIZED


BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(BASEDIR + '/.env')

secret = os.getenv('KEY')
algorithm = os.getenv('ALGORITHM')


def getAccessToken(email: str, password: str):
    '''
    Create an access token for header from email and password

    Parameters:
        email (str): email
        password (str): password

    Returns:
        str: access token

    '''
    payload = {'email': email, 'password': password}

    return jwt.encode(payload, key=secret, algorithm=algorithm)


def verifyToken(token: str = Header(...)):
    try:
        decoded = jwt.decode(token, algorithms=algorithm, key=secret)

        user = getUserByEmail(SessionLocal(), decoded['email'])
        if user is None or user.password != decoded['password']:
            raise HTTPException(
                                status_code=HTTP_401_UNAUTHORIZED,
                                detail='Incorrect token')

    except DecodeError or ExpiredSignatureError or KeyError:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail='Incorrect token'
        )

    return decoded

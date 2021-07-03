from sqlalchemy.orm import Session
from schema.user import UserCreate
from postgres.models import Users
from schema.plan import PlanCreate
from postgres.models import Plan
from sqlalchemy.sql.expression import update


def getUser(session: Session, id: int):
    '''
    Get a user by ID

    Parameters:
        session (Session): db session
        id (int): ID of user

    Returns:
        Users: Users object

    '''
    return session.query(Users).filter(Users.id == id).first()


def getUserByEmail(session: Session, email: str):
    '''
    Get a user by email

    Parameters:
        session (Session): db session
        email (str): email of user

    Returns:
        Users: Users object

    '''

    return session.query(Users).filter(Users.email == email).first()


def createUser(session: Session, user: UserCreate):

    '''
    Create a user

    Parameters:
        session (Session): db session
        user (UserCreate): UserCreate object

    Returns:
        None: return none

    '''
    passrword = user.password

    user.password = passrword

    userDB = Users(**user.dict())
    session.add(userDB)
    session.commit()
    session.refresh(userDB)
    return userDB


def addPlan(session: Session, id: int, plan: PlanCreate):
    '''
    Add a plan to user

    Parameters:
        session (Session): db session
        id (int): user ID
        plan (PlanCreate): a new plan

    Returns:
        None: no return value

    '''
    user = getUser(session, id)
    planDB = Plan(**plan.dict())
    user.plans.append(planDB)
    session.add(user)
    session.commit()


def updateUser(session: Session, id: int, properties: dict):
    '''
    Update user parameters

    Parameters:
        session (Session): db session
        id (int): user ID
        properties (dict): key-value properties

    Returns:
        None: no return value

    '''

    smt = update(Users).where(Users.id == id).values(**properties)
    session.execute(smt)

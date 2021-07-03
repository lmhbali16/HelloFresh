from sqlalchemy.orm import Session
from postgres.models import Plan
from schema.plan import PlanCreate, Plan as PlanAPI


def getPlanByUser(session: Session, id: int):
    '''
    Get plans by user ID

    Paramters:
        session (Session): db session
        id (int): id of user
    
    Returns:
        list: list of plans (Plan object)

    '''
    return session.query(Plan).filter(Plan.userid == id).all()


def getPlan(session: Session, id: int):
    '''
    Get a plan by ID

    Parameters:
        session (Session): db session
        id (int): plan ID

    Returns:
        Plan: a Plan object

    '''
    return session.query(Plan).filter(Plan.id == id).first()


def createPlan(session: Session, plan: PlanCreate):
    '''
    Create a plan

    Parameters:
        session (Session): db session
        plan (PlanCreate): PlaneCreate object

    Returns:
        None: No return value

    '''
    planDB = Plan(**plan.dict())
    session.add(planDB)
    session.commit()


def updatePlan(session: Session, plan: PlanAPI):
    '''
    Update a plan

    Parameters:
        session (Session): db session
        plan (PlanAPI): a schema.Plan object

    Returns:
        None: No return value

    '''
    planDB = Plan(**plan.dict())
    session.add(planDB)
    session.commit()


def deletePlan(session: Session, id: int):
    '''
    Delete a plan

    Parameters:
        session (Session): db session
        id (int): plan ID

    Returns:
        None: not return value

    '''
    plan = getPlan(session, id)
    session.delete(plan)
    session.commit()

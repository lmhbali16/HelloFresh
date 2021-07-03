from postgres.crud.planCrud import createPlan, deletePlan, getPlan, getPlanByUser, updatePlan
from postgres.crud.userCrud import getUserByEmail
from fastapi import APIRouter
from fastapi import Depends
from schema.plan import Plan, PlanCreate
from fastapi import Header
from starlette.status import HTTP_200_OK
from .token import verifyToken
from postgres.database import SessionLocal


planRouter = APIRouter(prefix='/plan', dependencies=[Depends(verifyToken)])


@planRouter.get('/')
def planMain(token: str = Header(...)):
    payload = verifyToken(token)
    email = payload['email']
    user = getUserByEmail(SessionLocal(), email)

    plans = getPlanByUser(SessionLocal(), user.id)

    return plans


@planRouter.get('/get')
def retrievePlan(id: int):
    return getPlan(SessionLocal(), id)


@planRouter.post('/delete')
def removePlan(id: int):
    deletePlan(SessionLocal(), id)
    return HTTP_200_OK


@planRouter.post('/update')
def planUpdate(plan: Plan):
    updatePlan(SessionLocal(), plan)


@planRouter.post('/create')
def planCreate(plan: PlanCreate):
    createPlan(SessionLocal(), plan)

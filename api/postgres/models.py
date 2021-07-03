from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import ARRAY, DATE, FLOAT, JSON
from .database import Base


association_table = Table(
                        'association',
                        Base.metadata,
                        Column('plan_id', Integer, ForeignKey('plans.id')),
                        Column('recipe_id', Integer, ForeignKey('recipe.id')))


class Recipe(Base):

    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, unique=True)
    ingredients = Column(ARRAY(JSON), nullable=False)
    nutrition = Column(ARRAY(JSON), nullable=False)
    preptime = Column(Integer, nullable=False)
    difficulty = Column(String, nullable=False)
    notincluded = Column(String, nullable=False)
    instruction = Column(ARRAY(String), nullable=False)


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(String)
    rating = Column(FLOAT)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    password = Column(String)
    email = Column(String, nullable=False, unique=True)
    plans = relationship("plans")


class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('users.id'))
    start = Column(DATE, nullable=False)
    end = Column(DATE, nullable=False)
    serve = Column(Integer, nullable=False)
    recipes = relationship('recipe', secondary=association_table)

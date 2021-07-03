from sqlalchemy.orm import Session
from postgres.models import Review
from sqlalchemy.sql.expression import update


def getReview(session: Session, id: int):
    '''
    Get a review by ID

    Parameters:
        session (Session): db session
        id (int): reivew ID

    Returns
        Review: Review object

    '''
    return session.query(Review).filter(Review.id == id).first()


def getReviewByUserID(session: Session, id: int):
    '''
    Get a review by UserID

    Parameters:
        session (Session): db session
        id (int): userID

    Returns:
        Review: Review object from postgres.models

    '''
    return session.query(Review).filter(Review.user == id).first()


def deleteReviewByUserID(session: Session, id: int):
    '''
    Delete a review by UserID

    Parameters:
        session (Session): db session
        id (int): userID

    Returns:
        None: no return value
    '''
    review = getReviewByUserID(session, id)
    session.delete(review)
    session.commit()


def updateReviewComment(session: Session, id: int, comment: str):
    '''
    Update comment of a review

    Parameters:
        session (Session): db session
        id (int): review ID
        comment (str): new comment

    Returns:
        None: not return value

    '''
    smt = update(Review).where(Review.user == id).values(comment=comment)
    session.execute(smt)


def updateReviewRating(session: Session, id: int, rating: str):
    '''
    Update a rating of a review

    Parameters:
        session (Session): db session
        id (int): ID of a review
        rating (float): review rating

    Returns:
        None: no return value

    '''
    smt = update(Review).where(Review.user == id).values(rating=rating)
    session.execute(smt)

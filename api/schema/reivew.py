from pydantic import BaseModel


class ReviewBase(BaseModel):
    user: int
    comment: str
    rating: float


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

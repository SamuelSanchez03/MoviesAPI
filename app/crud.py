from sqlalchemy.orm import Session
from . import models

# Read ALL categories
def get_categories(db: Session):
    return db.query(models.Category).all()

# Read ONE category by id
def get_category_by_id(db: Session, id: int):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    return category

# Read ALL movies
def get_movies(db: Session):
    return db.query(models.Movie).all()

# Read ONE movie by id
def get_movie_by_id(db: Session, id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    return movie

# Filter movies by category
def get_movies_by_category(db: Session, category_id: int):
    movies = db.query(models.Movie).filter(models.Movie.category_id == category_id).all()
    return movies

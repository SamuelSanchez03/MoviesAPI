from sqlalchemy import Column, Integer, Text, Numeric ,ForeignKey
from sqlalchemy.orm import relationship
from .database import database

class Category(database.Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    icon = Column(Text)

    movies = relationship("Movie", back_populates="category")


class Movie(database.Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    year = Column(Integer)
    image = Column(Text)
    description = Column(Text)
    director = Column(Text)
    imdb_score = Column(Numeric(3, 1))
    rating = Column(Text)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="movies")

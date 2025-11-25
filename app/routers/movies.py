from fastapi import APIRouter, Depends, HTTPException
from .. import crud
from .. import schemas
from sqlalchemy.orm import Session
from ..database.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Movie])
def get_all_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)

@router.get("/{id}", response_model=schemas.Movie)
def get_movie_by_id(id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_id(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found.")
    return movie

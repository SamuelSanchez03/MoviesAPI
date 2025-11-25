from fastapi import APIRouter, Depends, HTTPException
from .. import crud
from .. import schemas
from sqlalchemy.orm import Session
from ..database.database import get_db
router = APIRouter()

@router.get("/", response_model=list[schemas.Category])
def get_all_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get("/{id}", response_model=schemas.Category)
def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category

@router.get("/{id}/movies", response_model=list[schemas.Movie])
def get_movies_by_category(id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found.")
    return crud.get_movies_by_category(db, id)
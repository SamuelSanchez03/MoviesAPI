from fastapi import FastAPI
from . import models
from .database import database
from .routers import movies, categories

app = FastAPI(title="Movie API")

app.include_router(categories.router, prefix="/categories")
app.include_router(movies.router, prefix="/movies")

@app.get("/")
def root():
    return {"message": "Movie API working..."}
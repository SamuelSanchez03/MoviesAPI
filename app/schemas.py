from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    icon: str | None
    
class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    year: int
    image: str
    description: str
    category_id: int
    
class Movie(MovieBase):
    id: int
    
    class Config:
        from_attributes = True

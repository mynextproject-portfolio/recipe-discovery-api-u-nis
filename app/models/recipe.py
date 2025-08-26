from typing import List, Literal
from pydantic import BaseModel
import uuid

class RecipeCreate(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]
    prepTime: str
    cookTime: str
    difficulty: str
    cuisine: str

class Recipe(RecipeCreate):
    id: uuid.UUID   # server adds this
    

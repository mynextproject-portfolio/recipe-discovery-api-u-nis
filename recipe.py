from typing import List, Literal
from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]
    prepTime: str
    cookTime: str
    difficulty: str
    cuisine: str

class Recipe(RecipeCreate):
    id: int   # server adds this
    
# In-memory store (list of Recipe)
recipes: List[Recipe] = [
    Recipe(
        id=1,
        title="Spaghetti Carbonara",
        ingredients=["pasta", "eggs", "bacon", "cheese"],
        steps=["Cook pasta", "Mix eggs", "Combine all"],
        prepTime="10 minutes",
        cookTime="15 minutes",
        difficulty="Medium",
        cuisine="Italian",
    ),
    Recipe(
        id=2,
        title="Pancakes",
        ingredients=["flour", "milk", "egg", "baking powder", "sugar"],
        steps=["Mix dry", "Add wet", "Cook on griddle"],
        prepTime="5 minutes",
        cookTime="10 minutes",
        difficulty="Easy",
        cuisine="American",
    ),
]

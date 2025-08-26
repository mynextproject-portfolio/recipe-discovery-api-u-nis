from typing import List
from app.models.recipe import Recipe
import uuid

recipes: List[Recipe] = [
    Recipe(
        id=uuid.uuid4(),
        title="Spaghetti Carbonara",
        ingredients=["pasta", "eggs", "bacon", "cheese"],
        steps=["Cook pasta", "Mix eggs", "Combine all"],
        prepTime="10 minutes",
        cookTime="15 minutes",
        difficulty="Medium",
        cuisine="Italian",
    ),
    Recipe(
        id=uuid.uuid4(),
        title="Pancakes",
        ingredients=["flour", "milk", "egg", "baking powder", "sugar"],
        steps=["Mix dry", "Add wet", "Cook on griddle"],
        prepTime="5 minutes",
        cookTime="10 minutes",
        difficulty="Easy",
        cuisine="American",
    ),
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/recipes")
async def get_recipes():
    return recipes

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    return recipes[recipe_id]


recipes = [
    {
        "id": 0,
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
    },
    {
        "id": 1,
        "name": "Pancakes",
        "ingredients": ["flour", "milk", "egg", "baking powder", "sugar"],
    },
    {
        "id": 2,
        "name": "Chicken Salad",
        "ingredients": ["chicken breast", "lettuce", "tomato", "cucumber", "dressing"],
    }
]

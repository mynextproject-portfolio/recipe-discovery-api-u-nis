from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/recipes")
async def get_recipes():
    return recipes

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    if recipe_id > len(recipes) or recipe_id < 1:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes[recipe_id - 1]


recipes = [
    {
        "id": 1,
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
    },
    {
        "id": 2,
        "name": "Pancakes",
        "ingredients": ["flour", "milk", "egg", "baking powder", "sugar"],
    },
    {
        "id": 3,
        "name": "Chicken Salad",
        "ingredients": ["chicken breast", "lettuce", "tomato", "cucumber", "dressing"],
    }
]

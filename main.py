from fastapi import FastAPI, HTTPException
from recipe import recipes, RecipeCreate, Recipe


app = FastAPI()
next_id = len(recipes) + 1

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/recipes")
async def get_recipes():
    return recipes

@app.get("/recipes/search", status_code=200)
async def search_recipes(q: str):
    if q == "":
        return []
    results=[]
    q = q.lower()
    for r in recipes:
        if q in r.title.lower():
            results.append(r)


    return results


@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    for r in recipes:
        if r.id == recipe_id:
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/recipes", status_code=201)
async def create_recipe(recipe: RecipeCreate):
    global next_id
    next_id += 1
    new_recipe = Recipe(id=next_id, **recipe.dict())
    recipes.append(new_recipe)
    return new_recipe

@app.put("/recipes/{recipe_id}", status_code=200)
async def update_recipe(recipe_id: int, recipe: RecipeCreate):
    for r in recipes:
        if r.id == recipe_id:
            r.title = recipe.title
            r.ingredients = recipe.ingredients
            r.steps = recipe.steps
            r.prepTime = recipe.prepTime
            r.cookTime = recipe.cookTime
            r.difficulty = recipe.difficulty
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.delete("/recipes/{recipe_id}", status_code=204)
async def delete_recipe(recipe_id: int):
    for r in recipes:
        if r.id == recipe_id:
            recipes.remove(r)
            return
    raise HTTPException(status_code=404, detail="Recipe not found")


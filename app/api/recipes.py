from fastapi import APIRouter, HTTPException
from app.models.recipe import RecipeCreate, Recipe
from app.storage.memory import recipes
from typing import Optional
import uuid

router = APIRouter()



@router.get("/recipes")
async def get_recipes():
    return recipes

@router.get("/recipes/search", status_code=200)
async def search_recipes(q: Optional[str] = None):
    if not q:
        return []
    results=[]
    q = q.lower()
    for r in recipes:
        if q in r.title.lower():
            results.append(r)


    return results


@router.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: uuid.UUID):
    for r in recipes:
        if r.id == recipe_id:
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.post("/recipes", status_code=201)
async def create_recipe(recipe: RecipeCreate):
    new_recipe = Recipe(id=uuid.uuid4(), **recipe.model_dump())
    recipes.append(new_recipe)
    return new_recipe

@router.put("/recipes/{recipe_id}", status_code=200)
async def update_recipe(recipe_id: uuid.UUID, recipe: RecipeCreate):
    for r in recipes:
        if r.id == recipe_id:
            r.title = recipe.title
            r.ingredients = recipe.ingredients
            r.steps = recipe.steps
            r.prepTime = recipe.prepTime
            r.cookTime = recipe.cookTime
            r.difficulty = recipe.difficulty
            r.cuisine = recipe.cuisine
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete("/recipes/{recipe_id}", status_code=204)
async def delete_recipe(recipe_id: uuid.UUID):
    for r in recipes:
        if r.id == recipe_id:
            recipes.remove(r)
            return
    raise HTTPException(status_code=404, detail="Recipe not found")


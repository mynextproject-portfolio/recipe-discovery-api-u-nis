from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"

def test_create_recipe():
    response = client.post("/recipes", json={
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "American",
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Recipe"
    assert response.json()["ingredients"] == ["ingredient1", "ingredient2"]
    assert response.json()["steps"] == ["step1", "step2"]
    assert response.json()["prepTime"] == "10 minutes"
    assert response.json()["cookTime"] == "20 minutes"
    assert response.json()["difficulty"] == "Easy"
    assert response.json()["cuisine"] == "American"

def test_get_recipe_by_id():
    response = client.post("/recipes", json={
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "American",
    })
    assert response.status_code == 201
    recipe_id = response.json()["id"]
    response = client.get(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["id"] == recipe_id
    assert response.json()["title"] == "Test Recipe"
    assert response.json()["ingredients"] == ["ingredient1", "ingredient2"]
    assert response.json()["steps"] == ["step1", "step2"]
    assert response.json()["prepTime"] == "10 minutes"


def test_update_recipe():
    response = client.post("/recipes", json={
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "American",
    })
    assert response.status_code == 201
    recipe_id = response.json()["id"]
    response = client.put(f"/recipes/{recipe_id}", json={
        "title": "Updated Test Recipe", 
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "American",})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Recipe"
    

def test_search_recipe():
    response = client.post("/recipes", json={
        "title": "Test Recipe123",
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "American",
    })
    assert response.status_code == 201
    response = client.get("/recipes/search?q=Test")
    assert response.status_code == 200
    recipes = response.json()
    assert any(r["title"] == "Test Recipe123" for r in recipes)


def test_happy_path_crud_cycle():
    response = client.post("/recipes", json={
        "title": "pizza",
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "italian",
    })
    assert response.status_code == 201
    recipe_id = response.json()["id"]
    response = client.get(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["id"] == recipe_id
    assert response.json()["title"] == "pizza"
    response = client.get("/recipes/search?q=pizz")
    assert response.status_code == 200
    recipes = response.json()
    assert any(r["title"] == "pizza" for r in recipes)
    response = client.put(f"/recipes/{recipe_id}", json={
        "title": "pizza123", 
        "ingredients": ["ingredient1", "ingredient2"],
        "steps": ["step1", "step2"],
        "prepTime": "10 minutes",
        "cookTime": "20 minutes",
        "difficulty": "Easy",
        "cuisine": "italian",})
    assert response.status_code == 200
    response = client.get(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "pizza123"
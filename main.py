from fastapi import FastAPI, HTTPException
from typing import Optional
from app.api.health import router as health_router
from app.api.recipes import router as recipes_router

app = FastAPI()

app.include_router(health_router)
app.include_router(recipes_router)
"""API route definitions."""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HelloResponse(BaseModel):
    """Hello endpoint response model."""
    message: str


@router.get("/hello", response_model=HelloResponse)
async def hello():
    """Hello endpoint."""
    return HelloResponse(message="Hello from teste-completo!")


@router.get("/info")
async def info():
    """Application information endpoint."""
    return {
        "name": "teste-completo",
        "version": "1.0.0",
        "framework": "FastAPI",
        "python_version": "3.11+"
    }

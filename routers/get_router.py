# Import the APIRouter class from FastAPI
from fastapi import APIRouter
from services.first_service import Animal

# Define a router using APIRouter
router = APIRouter()
AnimalService = Animal("Simba","Lion")

# Define a route for the root endpoint "/"
@router.get("/")
async def read_root():
    # Return a simple message
    return {"message": "Hello, World!"}




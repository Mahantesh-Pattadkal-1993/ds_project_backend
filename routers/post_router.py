# Import the APIRouter class from FastAPI
from fastapi import APIRouter
import numpy as np
from pydantic import BaseModel


# Define a router using APIRouter
router = APIRouter()

# Define the input data structure
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float


# Define a route for the root endpoint "/"
@router.post("/predict")
async def predict(data: InputData):
    # Convert the input data to a numpy array
    input_data = [data.feature1, data.feature2, data.feature3]
    input_array = np.array(input_data)

    # Make the prediction
    prediction = np.sum(input_array)

    # Return the prediction as a JSON response
    return {"prediction": prediction}





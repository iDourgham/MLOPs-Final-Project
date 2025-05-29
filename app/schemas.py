from pydantic import BaseModel
from typing import List

class GestureInput(BaseModel):
    landmarks: List[float]

class GestureOutput(BaseModel):
    prediction: str

from pydantic import BaseModel
from typing import List

class GestureInput(BaseModel):
    features: List[float]

class PredictionOutput(BaseModel):
    encoded_label: int
    predicted_label: str

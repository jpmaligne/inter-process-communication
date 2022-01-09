from pydantic import BaseModel
from .prediction_entity import PredictionEntity


class PredictionVector(BaseModel):
    prediction_object: PredictionEntity
    prediction_rate: float

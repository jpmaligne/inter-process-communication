from pydantic import BaseModel
from .point import VectorPoint


class BaseVector(BaseModel):
    start: VectorPoint
    end: VectorPoint
    speed: float

from pydantic import BaseModel


class VectorPoint(BaseModel):
    x: int
    y: int

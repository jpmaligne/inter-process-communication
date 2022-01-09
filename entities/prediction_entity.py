from pydantic import BaseModel


class PredictionEntity(BaseModel):
    name: str

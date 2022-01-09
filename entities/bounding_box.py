from pydantic import BaseModel


class BoundingBox(BaseModel):
    x: int
    y: int
    width: int
    height: int

    # def __init__(self, x: int, y: int, width: int, height: int) -> None:
    #     super().__init__()
    #     self.x: int = x
    #     self.y: int = y
    #     self.width: int = width
    #     self.height: int = height

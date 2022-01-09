from pydantic import BaseModel
from datetime import datetime
from ..bounding_box import BoundingBox


class BaseTopicVector(BaseModel):
    timestamp: int = int(
        datetime.timestamp(datetime.now())
    )
    frame_id: int
    bounding_box: BoundingBox

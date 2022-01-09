from entities.bounding_box import BoundingBox
from ..base_vector.base_vector import BaseVector
from .base_topic_vector import BaseTopicVector


class MotionVector(BaseTopicVector):
    frame_id: int
    bounding_box: BoundingBox
    velocity_vector: BaseVector

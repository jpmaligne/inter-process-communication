from ..bounding_box import BoundingBox
from ..prediction_vector import PredictionVector
from .base_topic_vector import BaseTopicVector
from entities.bounding_box import BoundingBox


class DetectionVector(BaseTopicVector):
    frame_id: int
    bounding_box: BoundingBox
    prediction_vector: PredictionVector

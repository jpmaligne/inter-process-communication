from typing import Optional, Union
from pydantic import BaseModel
from entities.topics.topic_motion_vector import MotionVector
from entities.topics.topic_detection_vector import DetectionVector


class Logger(BaseModel):

    def publish(
        self,
        vector: Union[MotionVector, DetectionVector],
    ) -> None:
        if vector:
            print(vector)

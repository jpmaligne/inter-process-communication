# from typing import List, Optional
from pydantic import BaseModel
from entities.base_vector.base_vector import BaseVector
from entities.base_vector.point import VectorPoint
from entities.bounding_box import BoundingBox
from broker import Broker
from entities.topics.topic_motion_vector import MotionVector
from config import EVENTS, MOTION_DETECTED


class MotionDetector(BaseModel):
    broker: Broker

    def publish(self) -> None:
        try:
            start_point = VectorPoint(x=0, y=0)
            end_point = VectorPoint(x=1, y=1)
            velocity_vector = BaseVector(start=start_point, end=end_point, speed=2)
            bounding_box = BoundingBox(x=35, y=42, width=100, height=50)
            motion_vector = MotionVector(
                frame_id=1,
                bounding_box=bounding_box,
                velocity_vector=velocity_vector
            )
            self.broker.publish(event=EVENTS[MOTION_DETECTED], args=motion_vector)
        except KeyError:
            print(f"MotionDetector ERROR: Unknown event {MOTION_DETECTED}")

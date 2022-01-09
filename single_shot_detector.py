from typing import Optional
from pydantic import BaseModel
from broker import Broker
from config import EVENTS, MOTION_ANALYZED
from entities.prediction_entity import PredictionEntity
from entities.prediction_vector import PredictionVector
from entities.topics.topic_detection_vector import DetectionVector
from entities.topics.topic_motion_vector import MotionVector


class SingleShotDetector(BaseModel):
    broker: Broker

    def publish(self, motion_vector: MotionVector) -> None:
        try:
            detection_vector = self.analyze(motion_vector)
            if detection_vector:
                self.broker.publish(event=EVENTS[MOTION_ANALYZED], args=(detection_vector))
        except KeyError:
            print(f"MotionDetector ERROR: Unknown event {MOTION_ANALYZED}")

    def analyze(self, motion_vector: MotionVector) -> Optional[DetectionVector]:
        if motion_vector:
            # I guess some real science would happen here
            prediction_entity = PredictionEntity(name="car")
            prediction_vector = PredictionVector(
                prediction_object=prediction_entity,
                prediction_rate=0.5
            )
            return DetectionVector(
                frame_id=motion_vector.frame_id,
                bounding_box=motion_vector.bounding_box,
                prediction_vector=prediction_vector
            )

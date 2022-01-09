# from typing import List, Optional
from pydantic import BaseModel


class Broker(BaseModel):
    subscribers: dict = {}

    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cant be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            self.subscribers[event].append(callback)

    def publish(self, event, args) -> None:
        try:
            for callback in self.subscribers[event]:
                callback(args)
        except KeyError:
            print("MotionDetector ERROR: No subscribers")


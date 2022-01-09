from multiprocessing import Pool

from broker import Broker
from logger import Logger
from single_shot_detector import SingleShotDetector
from motion_detector import MotionDetector
from config import EVENTS, MOTION_ANALYZED, MOTION_DETECTED

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
        broker = Broker()
        MD = MotionDetector(broker=broker)
        SSD = SingleShotDetector(broker=broker)
        LOG = Logger()
        broker.subscribe(
            event=EVENTS[MOTION_DETECTED],
            callback=SSD.publish,
        )
        broker.subscribe(
            event=EVENTS[MOTION_ANALYZED],
            callback=LOG.publish,
        )

        res = pool.apply_async(MD.publish)
        try:
            res.get(timeout=1)
        except TimeoutError:
            print("timeoutError !!")

#   __filename__    __function_name__
from generateid import generate_id
from time import time
from random import random

class Timer:
    num_of_timers = 0

    def __init__(self):
        Timer.num_of_timers = Timer.num_of_timers + 1
        print("There have been %d timers created." % Timer.num_of_timers)

        self.id = generate_id(10)
        print("This timer has the id of '{}'.".format(self.id))
        
        self.current_time = 0
    
    def start(self):
        self.start_time = round(time(), 3)
        print("Timer no: {} has started timing.".format(self.id))

    def count(self):
        pass

    def stop(self):
        self.stop_time = round(time(), 3)
        print("Timer no: {} has stopped timing".format(self.id))
        time_difference = round(self.stop_time - self.start_time, 3)
        print("Timed: {}s".format(time_difference))

    def lap(self):
        pass

    def reset(self):
        pass


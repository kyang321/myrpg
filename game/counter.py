import time

class Counter(object):
    '''Object that is used to track timers (cooldowns, buffs, delay, etc)'''
    def __init__(self, duration):
        self.duration = duration
        self.start_time = time.time()
        self.timer_on = False

    def start(self):
        self.timer_on = True
        self.start_time = time.time()

    def update(self):
        if time.time() - self.start_time >= self.duration:
            self.timer_on = False
        

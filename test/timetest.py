import time

start_time = time.time()



class Counter(object):
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.cast_time = time.time()

    def cast(self):
        self.cast_time = time.time()
        print 'Cast time =', self.cast_time
        print 'Cooldown over!'

    def update(self):
        if time.time() - self.cast_time >= self.cooldown:
            print 'Time since last cast =', time.time() - self.cast_time
            self.cast()

counter = Counter(3.0)

while True:
    counter.update()
    time.sleep(1.0)


# A Real Time Clock
# -----------------
# Author          : Phil Hall
#                   https://github.com/rhubarbdog
# License         : Creative Commons 4.0
# First Published : May 2019

import time

class Clock():
    def __init__(self):
        self.future = None
        self.time_ = 0
        self.running = False

    def start(self):
        self.running = True
        self.future = time.ticks_add(time.ticks_ms(), 1000)

    def stop(self):
        self.running = False
        self.sleep(0)
        self.furure = None

    def time(self):
        return self.time_

    def reset(self):
        self.time_ = 0
        if self.running:
            self.start()

    def sleep(self, duration):
        current = time.ticks_ms()
        elapsed = time.ticks_add(current, duration)
        once = duration == 0
        while once or time.ticks_diff(elapsed, current) > 0:
            if not self.future is None:
                overrun = time.ticks_diff(self.future, current)
                if overrun <= 0:
                    while overrun < -1000:
                        overrun += 1000
                        self.time_ += 1
                    self.future = time.ticks_add(current,(1000 + overrun))
                    self.time_ += 1
            if once:
                once = False
            else:
                time.sleep_ms(10)
            current = time.ticks_ms()


if __name__ == '__main__':
    import microbit
    timer = Clock()

    # make multiple smal pauses but keep track of the time
    timer.start()
    for _ in range(10):
        timer.sleep(100)
    timer.stop()
    microbit.display.scroll(str(timer.time()))

    # or if your microbit is running flatout as simulated by
    # thie microbit.sleep(3000) make regular calls to
    # timer.sleep(0) to update the clock witout pausing
    timer.reset()
    timer.start()
    microbit.sleep(3100)
    timer.sleep(0) 
    microbit.display.scroll(str(timer.time()))
    

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
        self.sleep(0)
        return self.time_

    def reset(self):
        self.time = 0
        if self.running:
            self.start()

    def sleep(self, duration):
        current = time.ticks_ms()
        elapsed = time.ticks_add(current, duration)
        once = True
        while once or time.ticks_diff(elapsed, current) > 0:
            once = False
            if not self.future is None:
                overrun = time.ticks_diff(self.future, current)
                if overrun <= 0:
                    while overrun < -1000:
                        overrun += 1000
                        self.time_ += 1
                    self.future = time.ticks_add(current,(1000 + overrun))
                    self.time_ += 1

            time.sleep_ms(10)
            current = time.ticks_ms()


if __name__ == '__main__':
    import microbit
    timer = Clock()

    timer.start()
    time.sleep(4)
    timer.sleep(0)
    microbit.display.scroll(str(timer.time()))

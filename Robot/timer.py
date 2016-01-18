from threading import Thread
import time

class Timer():
    def __init__(self, delay, target=None):
        if not target is None:
            self.run = target

        self.delay = delay

        self.running = False
        self._t = Thread()

    def _run(self):
        while self.running:
            self.run()
            time.sleep(self.delay)

    def start(self):
        if self._t.is_alive() and not self.running:
            self._t.join()

        if not self._t.is_alive():
            self.running = True
            self._t = Thread(target=self._run)
            self._t.start()

    def pause(self):
        self.running = False

class MyTimer(Timer):
    def __init__(self):
        super().__init__(0.25)
        self.n = 0

    def run(self):
        self.n += 1
from multiprocessing import Queue

class Pipe:
    def __init__(self):
        self.queue = Queue()

    def push(self, data):
        self.queue.put(data)

    def pull(self):
        return self.queue.get()
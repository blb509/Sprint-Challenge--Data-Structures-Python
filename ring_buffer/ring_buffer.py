class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current = self.current + 1
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current = self.current + 1

    def get(self):
        toReturn = []
        for x in self.storage:
            if x is not None:
                toReturn.append(x)
        return toReturn


class RingBuffer:
    def __init__(self, size=64):
        self.size = size
        self.items = {}
        self.read_index = 0
        self.add_index = 0

    def add(self, item):
        if self.add_index == self.size:
            self.add_index = 0
            self.read_index += 1
        self.items[self.add_index] = item
        self.add_index += 1

    def get(self):
        if self.read_index == self.size:
            self.read_index = 0
        ret = self.items[self.read_index]
        self.items[self.read_index] = None
        self.read_index += 1
        return ret

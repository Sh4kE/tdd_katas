class RingBuffer:
    def __init__(self, size=64):
        self.size = size
        self.items = {}
        self.read_index = 0
        self.write_index = 0

    def add(self, item):
        if self.read_index in self.items.keys():
            if self.write_index == self.read_index and not (self.items[self.read_index] is None):
                self.read_index = self.increment_modulo(self.read_index)
        self.items[self.write_index] = item
        self.write_index = self.increment_modulo(self.write_index)

    def get(self):
        ret = self.items[self.read_index]
        self.items[self.read_index] = None
        self.read_index = self.increment_modulo(self.read_index)
        return ret

    def increment_modulo(self, index):
        return (index + 1) % self.size

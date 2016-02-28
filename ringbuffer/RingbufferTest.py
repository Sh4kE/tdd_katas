import unittest
from RingBuffer import RingBuffer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ringbuffer = RingBuffer(2)

    def test_create_ring_buffer(self):
        self.assertIsNotNone(self.ringbuffer)
        self.assertEquals(2, self.ringbuffer.size)

    def test_add_one_item(self):
        self.ringbuffer.add(1)
        self.assertEquals(1, self.ringbuffer.get())

    def test_add_two_items(self):
        self.ringbuffer.add(1)
        self.ringbuffer.add(2)
        self.assertEquals(1, self.ringbuffer.get())
        self.assertEquals(2, self.ringbuffer.get())

    def test_add_more_items_than_size(self):
        self.ringbuffer.add(1)
        self.ringbuffer.add(2)
        self.ringbuffer.add(3)
        self.assertEquals(2, self.ringbuffer.get())
        self.assertEquals(3, self.ringbuffer.get())
        self.assertEquals(None, self.ringbuffer.get())

    def test_first_read_then_add_full_buffer(self):
        self.ringbuffer.add(1)
        self.assertEquals(1, self.ringbuffer.get())
        self.ringbuffer.add(2)
        self.ringbuffer.add(3)
        self.assertEquals(2, self.ringbuffer.get())
        self.assertEquals(3, self.ringbuffer.get())
        self.assertEquals(None, self.ringbuffer.get())

    def test_first_read_then_add_more_items_than_size(self):
        self.ringbuffer.add(1)
        self.assertEquals(1, self.ringbuffer.get())
        self.ringbuffer.add(2)
        self.ringbuffer.add(3)
        self.ringbuffer.add(4)
        self.assertEquals(3, self.ringbuffer.get())
        self.assertEquals(4, self.ringbuffer.get())
        self.assertEquals(None, self.ringbuffer.get())


if __name__ == '__main__':
    unittest.main()

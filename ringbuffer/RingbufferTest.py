import unittest
from RingBuffer import RingBuffer


class RingBufferTestCase(unittest.TestCase):
    def setUp(self):
        self.ringbuffer = RingBuffer(2)

    def test_create_ring_buffer(self):
        self.assertIsNotNone(self.ringbuffer)
        self.assertEquals(2, self.ringbuffer.size)

    def test_addOneItem_SameItemReturns(self):
        self.ringbuffer.add(1)
        self.assertEquals(1, self.ringbuffer.get())

    def test_addFullBuffer_sameOrderReturns(self):
        self.ringbuffer.add(1)
        self.ringbuffer.add(2)
        self.assertEquals(1, self.ringbuffer.get())
        self.assertEquals(2, self.ringbuffer.get())

    def test_addOneMoreItemThanSize_FirstItemOverwritten(self):
        self.ringbuffer.add(1)
        self.ringbuffer.add(2)
        self.ringbuffer.add(3)
        self.assertEquals(2, self.ringbuffer.get())
        self.assertEquals(3, self.ringbuffer.get())
        self.assertEquals(None, self.ringbuffer.get())

    def test_firstAddAndReadThenAddFullBuffer_sameOrderAsPutInAfterRead(self):
        self.ringbuffer.add(1)
        self.assertEquals(1, self.ringbuffer.get())
        self.ringbuffer.add(2)
        self.ringbuffer.add(3)
        self.assertEquals(2, self.ringbuffer.get())
        self.assertEquals(3, self.ringbuffer.get())
        self.assertEquals(None, self.ringbuffer.get())

    def test_firstAddAndReadThenAddOneMoreItemThanSize_SecondItemOverwritten(self):
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

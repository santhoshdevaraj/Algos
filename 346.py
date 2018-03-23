# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque(maxlen=size)
        self.curr_sum = 0
        self.max_size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.max_size: self.curr_sum -= self.queue.popleft() 
        self.curr_sum += val
        self.queue.append(val)
        return float(self.curr_sum)/len(self.queue)

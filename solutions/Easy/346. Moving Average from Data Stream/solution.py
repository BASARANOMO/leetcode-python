class MovingAverage:
    def __init__(self, size: int):
        self.sum_val = 0
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum_val -= self.q.popleft()
        self.q.append(val)
        self.sum_val += val
        return self.sum_val / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

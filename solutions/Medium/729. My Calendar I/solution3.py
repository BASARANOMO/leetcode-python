class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l:
            # not booked
            return False
        if idx in self.lazy:
            # [l, r) booked
            return True
        if start <= l and r <= end:
            # [l, r) fully included in [start, end) but not all booked
            # part of [l, r) booked
            return idx in self.tree
        mid = (l + r) // 2
        return self.query(start, end, l, mid, 2 * idx) or self.query(
            start, end, mid + 1, r, 2 * idx + 1
        )

    def update(self, start: int, end: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            # no overlap
            return
        if start <= l and r <= end:
            # [l, r) fully included in [start, end)
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            # overlap == [l, r) contains 0 and 1
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree.add(idx)
            if idx * 2 in self.lazy and idx * 2 + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            # booked
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

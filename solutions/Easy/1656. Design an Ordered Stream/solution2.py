class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.streams = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.streams[idKey - 1] = value
        ans = []
        if self.ptr == idKey:
            while self.ptr <= len(self.streams) and self.streams[self.ptr - 1] != "":
                ans.append(self.streams[self.ptr - 1])
                self.ptr += 1

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

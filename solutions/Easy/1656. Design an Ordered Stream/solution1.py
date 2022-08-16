class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.idx_lst = [0] * n
        self.value_table = dict()

    def insert(self, idKey: int, value: str) -> List[str]:
        self.idx_lst[idKey - 1] = 1
        self.value_table[idKey - 1] = value
        ans = []
        if self.ptr == idKey:
            while self.ptr <= len(self.idx_lst) and self.idx_lst[self.ptr - 1] == 1:
                ans.append(self.value_table[self.ptr - 1])
                self.ptr += 1

        return ans

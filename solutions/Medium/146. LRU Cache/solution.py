from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_mem = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru_mem:
            self.lru_mem.move_to_end(key)
            return self.lru_mem[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_mem:
            self.lru_mem.move_to_end(key)
        self.lru_mem[key] = value
        if len(self.lru_mem) > self.capacity:
            self.lru_mem.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

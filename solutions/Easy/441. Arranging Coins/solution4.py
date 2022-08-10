class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + pow(8 * n + 1, 0.5)) / 2)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (r - l) // 2 + l
            tot = mid * (mid + 1) / 2
            if tot < n:
                l = mid + 1
            else:
                r = mid

        return l - 1 if l * (l + 1) / 2 > n else l

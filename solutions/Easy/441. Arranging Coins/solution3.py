class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (r - l) // 2 + l
            tot = mid * (mid + 1) / 2
            if tot + mid + 1 == n:
                return mid + 1
            elif tot < n and tot + mid + 1 >= n:
                return mid
            elif tot + mid + 1 < n:
                l = mid + 1
            else:
                r = mid

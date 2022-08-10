# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def check(l: int, r: int) -> int:
            if l == r:
                return l
            mid = (r - l) // 2 + l
            if isBadVersion(mid):
                return check(l, mid)
            else:
                return check(mid + 1, r)
        return check(0, n)
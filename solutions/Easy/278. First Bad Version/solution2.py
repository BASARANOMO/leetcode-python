# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            mid = (r - l) // 2 + l
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

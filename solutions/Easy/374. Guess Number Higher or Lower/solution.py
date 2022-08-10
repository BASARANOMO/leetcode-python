# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (r - l) // 2 + l
            val = guess(mid)
            if val == 0:
                return mid
            elif val < 0:
                r = mid
            else:
                l = mid + 1

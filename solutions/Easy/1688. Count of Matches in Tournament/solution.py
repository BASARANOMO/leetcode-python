class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:  # even
                res += n / 2
                n /= 2
            else:  # odd
                res += (n - 1) / 2
                n = (n - 1) / 2 + 1
        return int(res)

    def numberOfMatches_naive(self, n: int) -> int:
        return n - 1

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda x: x[1]):
            if cur < x:
                cur = y
                res += 1
        return res

class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(x) for x in s]
        tot = sum(s)
        n = len(s)
        ans, cur_sum = tot - 1, 0
        for i in range(0, n - 1):
            cur_sum += s[i]
            ans = max(ans, i + tot - cur_sum * 2 + 1)
        return ans

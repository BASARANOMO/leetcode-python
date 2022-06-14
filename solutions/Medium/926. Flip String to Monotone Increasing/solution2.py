class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        preSum = [0]
        for i in range(n):
            preSum.append(preSum[-1] + int(s[i]))
        return min(preSum[j] + (n - j) - (preSum[-1] - preSum[j]) for j in range(n + 1))
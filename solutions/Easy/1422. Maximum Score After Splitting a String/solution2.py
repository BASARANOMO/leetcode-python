class Solution:
    def maxScore(self, s: str) -> int:
        ans = score = (s[0] == "0") + s[1:].count("1")
        for ch in s[1:-1]:
            score += 1 if ch == "0" else -1
            ans = max(ans, score)
        return ans

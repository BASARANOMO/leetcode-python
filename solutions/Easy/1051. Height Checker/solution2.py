class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        maxVal = max(heights)
        cnt = [0] * (maxVal + 1)
        for h in heights:
            cnt[h] += 1
        idx = ans = 0
        for i in range(1, maxVal + 1):
            for j in range(cnt[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1
        
        return ans
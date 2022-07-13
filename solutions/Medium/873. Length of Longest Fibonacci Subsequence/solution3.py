class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr):
            for j in range(i + 1, n):
                if (arr[i] + arr[j]) in indices:
                    k = indices[arr[i] + arr[j]]
                    dp[j][k] = max(dp[i][j] + 1, 3)
                    ans = max(ans, dp[j][k])
        return ans
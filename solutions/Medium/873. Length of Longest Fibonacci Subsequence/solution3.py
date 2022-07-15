class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr):  # 以k, j为终点的子序列长度比以i, j为终点的子序列长1
            for j in range(i + 1, n):
                if (x + arr[j]) in indices:
                    k = indices[x + arr[j]]
                    dp[j][k] = max(dp[i][j] + 1, 3)
                    ans = max(ans, dp[j][k])
        return ans

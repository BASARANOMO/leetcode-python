class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr[::-1]):  # 以i, j为起点的子序列长度比以j, k为终点的子序列长1
            i = n - i - 1
            for j in range(n - 1, i, -1):
                if (x + arr[j]) in indices:
                    k = indices[x + arr[j]]
                    dp[i][j] = max(dp[j][k] + 1, 3)
                    ans = max(ans, dp[i][j])
        return ans

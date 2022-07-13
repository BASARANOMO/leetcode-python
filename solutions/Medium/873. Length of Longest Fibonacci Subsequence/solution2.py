class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr): # 以j, i为终点的子序列长度比以k, j为终点的子序列长1
            for j in range(i):
                if arr[j] * 2 <= x:
                    continue
                if x - arr[j] in indices:
                    k = indices[x - arr[j]]
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans
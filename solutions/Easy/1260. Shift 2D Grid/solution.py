class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        ans = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j + k
                ans[idx // n % m][idx % n] = grid[i][j]
        return ans
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        target = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    target += 1
                if grid[i][j] == 1:
                    xs, ys = i, j
        res = self.dfs(grid, target, xs, ys)
        return res

    def dfs(self, grid, target, i, j) -> int:
        m, n = len(grid), len(grid[0])
        if (i < 0) or (i >= m) or (j < 0) or (j >= n) or (grid[i][j] == -1):
            return 0
        if grid[i][j] == 2:
            if target == 0:
                return 1
            else:
                return 0
        grid[i][j] = -1
        target -= 1
        res = 0
        res += self.dfs(grid, target, i+1, j)
        res += self.dfs(grid, target, i, j+1)
        res += self.dfs(grid, target, i-1, j)
        res += self.dfs(grid, target, i, j-1)
        target += 1 # reset current state
        grid[i][j] = 0
        return res

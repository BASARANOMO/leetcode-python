class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp_matrix = [[float("-inf")] * n for _ in range(n)]
        dp_matrix[0][0] = grid[0][0]
        for t in range(1, 2 * n - 1):
            dp_matrix_curr = [[float("-inf")] * n for _ in range(n)]
            for i in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                for j in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    temp = grid[i][t - i]
                    if i != j:
                        temp += grid[j][t - j]
                    dp_matrix_curr[i][j] = (
                        max(
                            dp_matrix[prev_i][prev_j]
                            for prev_i in range(i - 1, i + 1)
                            for prev_j in range(j - 1, j + 1)
                            if prev_i >= 0 and prev_j >= 0
                        )
                        + temp
                    )
            dp_matrix = dp_matrix_curr
        return max(0, dp_matrix[-1][-1])

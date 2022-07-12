class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(m)]
        for x, y in indices:
            for j in range(n):
                mat[x][j] += 1
            for row in mat:
                row[y] += 1
        return sum(x % 2 for row in mat for x in row)


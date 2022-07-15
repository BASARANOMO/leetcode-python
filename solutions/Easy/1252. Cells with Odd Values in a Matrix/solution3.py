class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        oddx = sum(row % 2 for row in rows)
        oddy = sum(col % 2 for col in cols)
        return oddx * (n - oddy) + oddy * (m - oddx)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val_min, val_max = min(m-1, n-1), max(m-1, n-1)
        return int(self.factorial(val_max+val_min, val_min, False) / self.factorial(val_min, val_min, False))


    def factorial(self, val: int, nums: int, ascendent: bool) -> int:
        if nums > 0:
            if ascendent:
                return self.factorial(val+1, nums-1, ascendent) * val
            else:
                return self.factorial(val-1, nums-1, ascendent) * val

        return 1

    # DP space O(m * n)
    def uniquePaths_DP(self, m: int, n: int) -> int:
        if (m == 0) or (n == 0):
            return 0
        dp_matrix = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j-1]
        return dp_matrix[-1][-1]

    # DP space O(n)
    def uniquePaths_DP_opt(self, m: int, n: int) -> int:
        if (m == 0) or (n == 0):
            return 0
        dp_matrix = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp_matrix[j] = dp_matrix[j] + dp_matrix[j-1]
        return dp_matrix[-1]

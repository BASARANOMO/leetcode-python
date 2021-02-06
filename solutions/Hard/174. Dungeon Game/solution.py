class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp_matrix = [[0 for _ in range(n)] for _ in range(m)]
        dp_matrix[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(1, m):
            dp_matrix[m-i-1][-1] = max(1, dp_matrix[m-i][-1]-dungeon[m-i-1][-1])
        for j in range(1, n):
            dp_matrix[-1][n-j-1] = max(1, dp_matrix[-1][n-j]-dungeon[-1][n-j-1])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp_matrix[i][j] = max(1,
                                     min(dp_matrix[i+1][j], dp_matrix[i][j+1]) - dungeon[i][j])
        return dp_matrix[0][0]

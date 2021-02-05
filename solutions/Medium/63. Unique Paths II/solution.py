class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp_matrix = [[0 for _ in range(n)] for _ in range(m)]
        dp_matrix[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if (dp_matrix[i-1][0] == 1) and (obstacleGrid[i][0] == 0):
                dp_matrix[i][0] = 1
        for j in range(1, n):
            if (dp_matrix[0][j-1] == 1) and (obstacleGrid[0][j] == 0):
                dp_matrix[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp_matrix[i][j] = 0
                else:
                    dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j-1]
        return dp_matrix[-1][-1]

    def uniquePathsWithObstacles_opt(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            obstacleGrid[i][0] = 1 - obstacleGrid[i][0]
            if obstacleGrid[i-1][0] == 0:
                obstacleGrid[i][0] = 0
        for j in range(1, n):
            obstacleGrid[0][j] = 1 - obstacleGrid[0][j]
            if obstacleGrid[0][j-1] == 0:
                obstacleGrid[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

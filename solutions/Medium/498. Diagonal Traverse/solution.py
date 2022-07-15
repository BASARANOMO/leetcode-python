class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                nrow = 0 if i < n else i - n + 1
                ncol = i if i < n else n - 1
                while nrow < m and ncol >= 0:
                    ans.append(mat[nrow][ncol])
                    ncol -= 1
                    nrow += 1
            else:
                nrow = i if i < m else m - 1
                ncol = 0 if i < m else i - m + 1
                while ncol < n and nrow >= 0:
                    ans.append(mat[nrow][ncol])
                    nrow -= 1
                    ncol += 1
        return ans

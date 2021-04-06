class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        visited = [0] * n
        self.backtracking(n, visited, 1)
        return self.res

    def backtracking(self, n, visited, pos) -> int:
        if pos > n:
            self.res += 1
        for i in range(1, n + 1):
            if (visited[i - 1] == 0) and (i % pos == 0 or pos % i == 0):
                visited[i - 1] = 1
                self.backtracking(n, visited, pos + 1)
                visited[i - 1] = 0

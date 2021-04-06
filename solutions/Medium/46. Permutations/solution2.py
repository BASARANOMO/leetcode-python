class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [0] * n
        self.backtracking(n, nums, visited, 0, [], res)
        return res

    def backtracking(self, n, nums, visited, pos, curr, res):
        if len(curr) == n:
            res.append(curr.copy())
        for i in range(0, n):
            if visited[i] == 0:
                curr.append(nums[i])
                visited[i] = 1
                self.backtracking(n, nums, visited, pos + 1, curr, res)
                curr.pop()
                visited[i] = 0

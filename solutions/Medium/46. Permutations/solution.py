class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        visited = [0] * n
        self.helper(n, nums, visited, 0, [])
        return self.res


    def helper(self, n, nums, visited, pos, curr):
        if (len(curr) == n):
            self.res.append(curr.copy())
        for i in range(0, n):
            if (visited[i] == 0):
                curr.append(nums[i])
                visited[i] = 1
                self.helper(n, nums, visited, pos+1, curr)
                curr.pop()
                visited[i] = 0

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        visited = [0] * n
        for i in range(n):
            cnt = 0
            while not visited[i]:
                visited[i] = 1
                i = nums[i]
                cnt += 1
            ans = max(cnt, ans)
            # visited = [0] * n
            # because all the values of nums are unique
        return ans
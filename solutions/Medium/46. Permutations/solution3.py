class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, curr, res):
        if not nums:
            res.append(curr)
        for i in range(len(nums)):
            self.backtracking(nums[:i] + nums[i + 1 :], curr + [nums[i]], res)

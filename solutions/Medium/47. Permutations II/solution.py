class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res)
        return list(set([tuple(t) for t in res]))

    def backtracking(self, nums, curr, res):
        if not nums:
            res.append(curr)
        for i in range(len(nums)):
            self.backtracking(nums[:i]+nums[i+1:], curr+[nums[i]], res)

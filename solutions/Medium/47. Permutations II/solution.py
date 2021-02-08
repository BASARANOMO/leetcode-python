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

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []
        num_groups = {}
        for num in nums:
            if not num_groups.get(num):
                num_groups[num] = 1
            else:
                num_groups[num] += 1
        self.backtracking(len(nums), num_groups, [], res)
        return res

    def backtracking2(self, n, num_groups, curr, res):
        if len(curr) == n:
            res.append(curr[:])
        for num in num_groups:
            if num_groups[num] > 0:
                num_groups[num] -= 1
                curr.append(num)
                self.backtracking(n, num_groups, curr, res)
                num_groups[num] += 1
                curr.pop()

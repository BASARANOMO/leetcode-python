class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pre = 0
        for i, num in enumerate(nums):
            if num >= n - i and pre < n - i:
                return n - i
            pre = num
        return -1
        
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = float("inf")
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            min_val = min(min_val, cur)
        return -min_val + 1 if min_val < 0 else 1

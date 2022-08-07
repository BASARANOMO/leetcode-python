class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums_sorted_reverse = sorted(nums)[::-1]
        sum_nums = sum(nums)
        cur_sum = 0
        for i, num in enumerate(nums_sorted_reverse):
            cur_sum += num
            if cur_sum > sum_nums / 2:
                return nums_sorted_reverse[: i + 1]

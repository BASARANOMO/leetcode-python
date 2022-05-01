class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            max_val = max(nums[i] + k, nums[-1] - k)
            min_val = min(nums[0] + k, nums[i + 1] - k)
            ans = min(max_val - min_val, ans)
        return ans
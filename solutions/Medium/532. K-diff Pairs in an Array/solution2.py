class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, y, res = len(nums), 0, 0
        for x in range(n):
            if x == 0 or nums[x] != nums[x - 1]:
                while y < n and (nums[y] < nums[x] + k or y <= x):
                    y += 1
                if y < n and nums[y] == nums[x] + k:
                    res += 1
        return res

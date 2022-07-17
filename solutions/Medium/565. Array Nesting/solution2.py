class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] >= 0:
                # can not do i = nums[i] because reference passed here
                num = nums[i]
                nums[i] = -1
                i = num
                cnt += 1
            ans = max(cnt, ans)
            # visited = [0] * n
            # because all the values of nums are unique
        return ans
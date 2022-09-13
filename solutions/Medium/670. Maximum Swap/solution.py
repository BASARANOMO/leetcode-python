class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i, val in enumerate(nums[::-1]):
            if val > nums[maxIdx]:
                maxIdx = n - i - 1
            elif val < nums[maxIdx]:
                idx1, idx2 = n - i - 1, maxIdx
        if idx1 < 0:
            return num
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        return int("".join(nums))

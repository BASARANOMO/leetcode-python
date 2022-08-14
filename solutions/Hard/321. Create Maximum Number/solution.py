class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n, m = len(nums1), len(nums2)
        ans = [0] * k
        for t in range(k + 1):
            if t <= n and k - t <= m:
                mntn_stk1 = self.pickMax(nums1, t)
                mntn_stk2 = self.pickMax(nums2, k - t)
                ans = max(ans, self.maxMerge(mntn_stk1, mntn_stk2))
        return ans

    def pickMax(self, nums: List[int], k: int) -> List[int]:
        i, n = 0, len(nums)
        mntn_stk = []
        num_to_drop = n - k
        while i < n:
            val = nums[i]
            while mntn_stk and mntn_stk[-1] < val and num_to_drop > 0:
                mntn_stk.pop()
                num_to_drop -= 1
            i += 1
            mntn_stk.append(val)
        return mntn_stk[:k]

    def maxMerge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        p1 = p2 = 0
        ans = []
        while p1 < n and p2 < m:
            num1, num2 = nums1[p1], nums2[p2]
            if nums1[p1:] > nums2[p2:]:
                ans.append(num1)
                p1 += 1
            else:
                ans.append(num2)
                p2 += 1
        if p1 < n:
            ans += nums1[p1:]
        if p2 < m:
            ans += nums2[p2:]
        return ans

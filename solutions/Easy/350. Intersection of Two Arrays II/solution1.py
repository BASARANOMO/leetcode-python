class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter()
        cnt2 = collections.Counter()
        for num in nums1:
            cnt1[num] += 1
        for num in nums2:
            cnt2[num] += 1
        ans = []
        if len(cnt1) < len(cnt2):
            for x in cnt1:
                if x in cnt2:
                    ans += [x] * min(cnt1[x], cnt2[x])
        else:
            for x in cnt2:
                if x in cnt1:
                    ans += [x] * min(cnt1[x], cnt2[x])
        return ans

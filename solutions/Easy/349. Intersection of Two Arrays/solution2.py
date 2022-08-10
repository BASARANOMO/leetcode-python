class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        ans, pre_val = [], None
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2] and nums1[p1] != pre_val:
                ans.append(nums1[p1])
                pre_val = nums1[p1]
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return ans

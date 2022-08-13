class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mntn_stk = []
        for num in arr:
            if len(mntn_stk) == 0 or mntn_stk[-1] <= num:
                mntn_stk.append(num)
            else:
                cur_max = mntn_stk.pop()
                while mntn_stk and mntn_stk[-1] > num:
                    mntn_stk.pop()
                mntn_stk.append(cur_max)
        return len(mntn_stk)

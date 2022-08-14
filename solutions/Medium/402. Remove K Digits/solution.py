class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i, n = 0, len(num)
        if n <= k:
            return "0"
        mntn_stk = []
        while i < n:
            val = num[i]
            while mntn_stk and mntn_stk[-1] > val and k > 0:
                mntn_stk.pop()
                k -= 1
            i += 1
            mntn_stk.append(val)
        if k > 0:
            mntn_stk = mntn_stk[:-k]
        return "".join(mntn_stk).lstrip("0") or "0"

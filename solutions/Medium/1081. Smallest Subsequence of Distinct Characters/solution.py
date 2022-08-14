class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = collections.Counter(s)
        mntn_stk = []
        i, n = 0, len(s)
        while i < n:
            ch = s[i]
            if ch not in mntn_stk:
                while mntn_stk and mntn_stk[-1] > ch and cnt[mntn_stk[-1]] > 0:
                    mntn_stk.pop()
                mntn_stk.append(ch)
            cnt[ch] -= 1
            i += 1
        return "".join(mntn_stk)

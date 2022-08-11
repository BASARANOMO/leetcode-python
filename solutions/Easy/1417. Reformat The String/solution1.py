class Solution:
    def reformat(self, s: str) -> str:
        stk1 = []
        stk2 = []
        for i, ch in enumerate(s):
            if ch.isdigit():
                stk1.append(ch)
            else:
                stk2.append(ch)
        if abs(len(stk1) - len(stk2)) > 1:
            return ""
        ans = []
        for i in range(min(len(stk1), len(stk2))):
            ans.append(stk1.pop())
            ans.append(stk2.pop())
        ans += stk1
        ans = stk2 + ans
        return "".join(ans)

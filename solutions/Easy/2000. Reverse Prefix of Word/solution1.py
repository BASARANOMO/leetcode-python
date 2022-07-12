class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stk = []
        if_found = False
        for idx, char in enumerate(word):
            stk.append(char)
            if char == ch:
                if_found = True
                res = []
                while stk:
                    res.append(stk.pop())
                res = ''.join(res) + word[idx + 1:]
                break
        if if_found:
            return res
        else:
            return word

class Solution:
    def isValid(self, code: str) -> bool:
        tags_stk = []
        i, n = 0, len(code)
        while i < n:
            if code[i] != "<":
                if not tags_stk:
                    # no begin tag in stack
                    return False
                i += 1
                continue
            if i == n - 1:
                # last char, not wrapped by closed tag
                return False
            if code[i + 1] == "/":
                # end tag
                j = code.find(">", i)
                if j == -1:
                    # not found
                    return False
                tagname = code[i + 2 : j]
                if not tags_stk or tags_stk[-1] != tagname:
                    return False
                tags_stk.pop()
                i = j + 1
                if not tags_stk and i != n:
                    # no begin tag in stack but code not been traversed
                    return False
            elif code[i + 1] == "!":
                if not tags_stk:
                    return False
                cdata = code[i + 2 : i + 9]
                if cdata != "[CDATA[":
                    return False
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 1
            else:
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 1 : j]
                if not 1 <= len(tagname) <= 9 or not all(ch.isupper() for ch in tagname):
                    return False
                tags_stk.append(tagname)
                i = j + 1
        return not tags_stk

                
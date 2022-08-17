class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        while i >= 0 or j >= 0:
            val1, val2 = 0, 0
            if i >= 0:
                val1 = int(a[i])
            if j >= 0:
                val2 = int(b[j])
            tmp = val1 + val2 + carry
            if tmp > 1:
                carry = 1
                tmp -= 2
            else:
                carry = 0
            ans.append(str(tmp))
            i -= 1
            j -= 1
        if carry:
            ans.append("1")
        return "".join(ans[::-1])

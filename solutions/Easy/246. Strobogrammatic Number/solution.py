class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        corr = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        l, r = 0, len(num) - 1
        while l <= r:
            num1 = int(num[l])
            num2 = int(num[r])
            if num1 not in corr or num2 not in corr or corr[num1] != num2:
                return False
            l += 1
            r -= 1
        return True

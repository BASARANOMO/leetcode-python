class Solution:
    def reformat(self, s: str) -> str:
        i, n = 1, len(s)
        s = list(s)
        sum_digit = sum(ch.isdigit() for ch in s)
        sum_alpha = n - sum_digit
        if abs(sum_digit - sum_alpha) > 1:
            return ""
        flag = sum_digit > sum_alpha
        for j in range(0, n, 2):
            if s[j].isdigit() != flag:
                while s[i].isdigit() != flag:
                    i += 2
                s[i], s[j] = s[j], s[i]
        return "".join(s)

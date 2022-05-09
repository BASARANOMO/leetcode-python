class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min_val, max_val = 0, len(s)
        ans = []
        for i in range(len(s)):
            if s[i] == "I":
                ans.append(min_val)
                min_val += 1
            else:
                ans.append(max_val)
                max_val -= 1
        ans.append(max_val)
        return ans
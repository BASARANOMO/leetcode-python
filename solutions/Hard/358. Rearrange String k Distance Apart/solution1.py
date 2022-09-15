class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        charCnts = dict()
        for ch in s:
            if ch in charCnts:
                charCnts[ch] += 1
            else:
                charCnts[ch] = 1
        chVec = []
        for ch, cnt in charCnts.items():
            chVec.append([cnt, ch])
        res = ""
        while True:
            chVec.sort(key=lambda x: -x[0])
            cnt = 0
            for i in range(len(chVec)):
                if chVec[i][0] == 0:
                    break
                res += chVec[i][1]
                cnt += 1
                chVec[i][0] -= 1
                if cnt == k:
                    break
            if len(res) == len(s):
                return res
            if cnt < k:
                return ""
        return res

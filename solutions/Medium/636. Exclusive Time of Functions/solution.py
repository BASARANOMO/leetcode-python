class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk = []
        for log in logs:
            idx, tp, timestamp = log.split(":")
            idx, timestamp = int(idx), int(timestamp)
            if tp == "start":
                if stk:
                    ans[stk[-1][0]] += timestamp - stk[-1][1]
                    stk[-1][1] = timestamp
                stk.append([idx, timestamp])
            else:
                i, t = stk.pop()
                ans[i] += timestamp - t + 1
                if stk:
                    stk[-1][1] = timestamp + 1
        return ans

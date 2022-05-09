class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
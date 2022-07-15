class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        def diffOne(s: str, t: str) -> bool:
            return sum(x != y for x, y in zip(s, t)) == 1

        m = len(bank)
        adj = [[] for _ in range(m)]
        end_idx = -1
        for i, s in enumerate(bank):
            if s == end:
                end_idx = i
            for j in range(i + 1, m):
                if diffOne(s, bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        if end_idx == -1:
            return -1

        q = [i for i, s in enumerate(bank) if diffOne(start, s)]
        visited = set(q)
        step = 1
        while q:
            temp = q
            q = []
            for cur in temp:
                if cur == end_idx:
                    return step
                for nxt in adj[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            step += 1
        return -1

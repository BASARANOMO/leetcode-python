class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        ch_freq = collections.Counter(s)
        ch_heap = [(-1 * freq, ch) for ch, freq in ch_freq.items()]
        heapq.heapify(ch_heap)
        q = collections.deque()
        res = ""
        while ch_heap:
            freq, ch = heapq.heappop(ch_heap)
            freq *= -1
            res += ch
            q.append((freq - 1, ch))
            if len(q) == k:
                freq, ch = q.popleft()
                if freq > 0:
                    heapq.heappush(ch_heap, (-1 * freq, ch))
        return res if len(res) == len(s) else ""

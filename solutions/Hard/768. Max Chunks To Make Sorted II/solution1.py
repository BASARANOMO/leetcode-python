class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        arr_sorted = sorted(arr)
        cnt = Counter()
        for i in range(len(arr)):
            cnt[arr[i]] += 1
            if cnt[arr[i]] == 0:
                del cnt[arr[i]]
            cnt[arr_sorted[i]] -= 1
            if cnt[arr_sorted[i]] == 0:
                del cnt[arr_sorted[i]]
            if len(cnt) == 0:
                res += 1
        return res

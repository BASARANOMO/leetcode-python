class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        num_block = 0
        cur_max = 0
        i, n = 0, len(arr)
        while i < n:
            cur_max = max(cur_max, arr[i])
            if cur_max == i:
                num_block += 1
            i += 1
        return num_block

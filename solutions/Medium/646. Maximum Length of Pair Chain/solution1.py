class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        arr = []
        for x, y in pairs:
            i = bisect_left(arr, x)
            if i < len(arr):
                arr[len(arr) - 1] = min(arr[len(arr) - 1], y)
            else:
                arr.append(y)
        return len(arr)

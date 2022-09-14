class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        i = int(n * 0.05)
        j = n - int(n * 0.05)
        return sum(arr[i:j]) / (j - i)

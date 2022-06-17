class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        stk = [0] * n
        i, top = -1, 0
        while top < n:
            i += 1
            stk[top] = arr[i]
            top += 1
            if arr[i] == 0 and top < n:
                stk[top] = arr[i]
                top += 1
        i = 0
        while i < n:
            arr[i] = stk[i]
            i += 1

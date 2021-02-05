class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val_min, val_max = min(m-1, n-1), max(m-1, n-1)
        return int(self.factorial(val_max+val_min, val_min, False) / self.factorial(val_min, val_min, False))


    def factorial(self, val: int, nums: int, ascendent: bool) -> int:
        if nums > 0:
            if ascendent:
                return self.factorial(val+1, nums-1, ascendent) * val
            else:
                return self.factorial(val-1, nums-1, ascendent) * val

        return 1

# 899. Orderly Queue

## Solution

Simulation

If `k > 1`, we can swap the positions of any two adjacent elements, which means that we can achieve bubble sort

Time complexity:
- if `k == 1`: `O(n^2)`
- if `k > 1`: `O(nlogn)`

Space complexity:
- if `k == 1`: `O(n)`
- if `k > 1`: `O(logn)`

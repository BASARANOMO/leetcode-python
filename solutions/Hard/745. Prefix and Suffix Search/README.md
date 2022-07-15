# 745. Prefix and Suffix Search

## Solution1

Trie

Time complexity of `__init__()`: `O(sum_{i=0}^{n-1} (w_i)^2)` where `w_i` is the length of the `i`-th word

Time complexity of `f()`: `O(max(p, s))` where `p` and `s` is the length of `pref` and `suff`

Space complexity of `__init__()`:: `O(sum_{i=0}^{n-1} (w_i)^2)`

Space complexity of `f()`:: `O(1)`

## Solution2

Two trie

## Solution3

Hash table + brute force

Time complexity of `__init__()`: `O(sum_{i=0}^{n-1} (w_i)^3)`

Time complexity of `f()`: `O(p + s)`

Space complexity of `__init__()`:: `O(sum_{i=0}^{n-1} (w_i)^3)`

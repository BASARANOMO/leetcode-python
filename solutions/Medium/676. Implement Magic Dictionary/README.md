# 676. Implement Magic Dictionary

## Solution1

Brute force + enumeration

Time complexity of `buildDict()` method: `O(n * l)` where `n` and `l` are the length of `dictionary` and the average length of all words in `dictionary`, respectively.

Time complexity of `search()` method: `O(n * l)`

Space complexity: `O(n * l)`

## Solution2

Trie

Time complexity of `buildDict()` method: `O(n * l)` where `n` and `l` are the length of `dictionary` and the average length of all words in `dictionary`, respectively.

Time complexity of `search()` method: `O(l * m)` where `m` is the length of `searchWord`

Space complexity: `O(n * l)`

# 526. Beautiful Arrangement
Suppose you have n integers labeled ```1``` through ```n```. A permutation of those ```n``` integers perm (__1-indexed__) is considered a beautiful arrangement if for every ```i``` (```1 <= i <= n```), either of the following is true:

- ```perm[i]``` is divisible by ```i```.
- ```i``` is divisible by ```perm[i]```.
-
Given an integer ```n```, return ___the __number__ of the __beautiful arrangements__ that you can construct.___

__Example 1:__
```
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
```

__Example 2:__
```
Input: n = 1
Output: 1
```

__Constraints:__
- ```1 <= n <= 15```

## Solution
Backtracking

## Notes
Brute force (consider every permutation) is generally not acceptable (time limit exceeded).

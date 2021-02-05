# 63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

__Example 1:__

![Example 1](https://github.com/BASARANOMO/leetcode-python/blob/main/solutions/Medium/63.%20Unique%20Paths%20II/robot1.jpg)
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

__Example 2:__

![Example 2](https://github.com/BASARANOMO/leetcode-python/blob/main/solutions/Medium/63.%20Unique%20Paths%20II/robot2.jpg)
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

__Constraints:__
- ```m == obstacleGrid.length```
- ```n == obstacleGrid[i].length```
- ```1 <= m, n <= 100```
- ```obstacleGrid[i][j]``` is ```0``` or ```1```.

# Solution
Dynamic programming

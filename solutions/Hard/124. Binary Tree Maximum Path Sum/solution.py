# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftMaxSum = max(0, dfs(root.left))
            rightMaxSum = max(0, dfs(root.right))
            nonlocal maxSum
            maxSum = max(maxSum, leftMaxSum + rightMaxSum + root.val)
            return max(leftMaxSum, rightMaxSum) + root.val

        dfs(root)
        return maxSum

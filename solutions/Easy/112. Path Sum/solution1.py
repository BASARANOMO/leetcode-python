# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], curSum: int, targetSum: int) -> bool:
            if not root:
                return False
            curSum += root.val
            if curSum == targetSum and not root.left and not root.right:
                return True
            return dfs(root.left, curSum, targetSum) or dfs(
                root.right, curSum, targetSum
            )

        return dfs(root, 0, targetSum)

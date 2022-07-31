# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(root: Optional[TreeNode], level: int) -> None:
            if level == len(sums):
                sums.append(root.val)
            else:
                sums[level] += root.val
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)
        return sums.index(max(sums)) + 1

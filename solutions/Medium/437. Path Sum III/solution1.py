# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root: TreeNode, targetSum: int) -> int:
            if root is None:
                return 0
            ret = 0
            if root.val == targetSum:
                ret += 1
            ret += dfs(root.left, targetSum - root.val)
            ret += dfs(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0
        ret = dfs(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        return ret

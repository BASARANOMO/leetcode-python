# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = list()
        cur = list()

        def dfs(root: Optional[TreeNode], targetSum: int) -> None:
            if not root:
                return
            cur.append(root.val)
            targetSum -= root.val
            if targetSum == 0 and not root.left and not root.right:
                res.append(cur[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            cur.pop()

        if root:
            dfs(root, targetSum)
        return res

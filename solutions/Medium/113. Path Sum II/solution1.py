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

        def dfs(root: Optional[TreeNode], curSum: int, targetSum: int) -> None:
            if not root:
                return
            if curSum == targetSum and not root.left and not root.right:
                res.append(cur[:])
            if root.left:
                curSum += root.left.val
                cur.append(root.left.val)
                dfs(root.left, curSum, targetSum)
                curSum -= root.left.val
                cur.pop()
            if root.right:
                curSum += root.right.val
                cur.append(root.right.val)
                dfs(root.right, curSum, targetSum)
                curSum -= root.right.val
                cur.pop()

        if root:
            cur.append(root.val)
            dfs(root, root.val, targetSum)
        return res

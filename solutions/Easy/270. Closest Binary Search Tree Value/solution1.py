# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode], target: float, min_remain: float) -> None:
            if not root:
                return
            cur_remain = root.val - target
            if abs(cur_remain) < min_remain:
                nonlocal ans
                ans = root.val
                min_remain = abs(cur_remain)
            if cur_remain < 0:
                dfs(root.right, target, min_remain)
            else:
                dfs(root.left, target, min_remain)

        dfs(root, target, float("inf"))
        return ans

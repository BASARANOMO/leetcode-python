# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        ans = 0

        def dfs(root: TreeNode, cur_level: int) -> None:
            if not root:
                return
            nonlocal max_level, ans
            if cur_level > max_level:
                max_level = cur_level
                ans = root.val
            elif cur_level == max_level:
                ans += root.val
            dfs(root.left, cur_level + 1)
            dfs(root.right, cur_level + 1)

        dfs(root, 0)
        return ans

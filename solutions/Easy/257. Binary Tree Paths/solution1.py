# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = list()
        path = list()

        def dfs(root: TreeNode) -> None:
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(path))
            dfs(root.left)
            dfs(root.right)
            path.pop()

        if root:
            dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()
        # dfs
        def dfs(root: TreeNode, row: int, col: int) -> None:
            if root is None:
                return None
            nodes.append((col, row, root.val))
            if root.left:
                dfs(root.left, row + 1, col - 1)
            if root.right:
                dfs(root.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()  # row -> col -> val
        ans, lastcol = list(), float("-inf")
        for col, row, val in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(val)
        return ans

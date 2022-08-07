# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        cur_depth = 1
        q = [root]
        while q:
            cur_q = []
            cur_depth += 1
            if cur_depth == depth:
                for node in q:
                    node.left = TreeNode(val, left=node.left)
                    node.right = TreeNode(val, right=node.right)
                return root
            else:
                for node in q:
                    if node.left:
                        cur_q.append(node.left)
                    if node.right:
                        cur_q.append(node.right)
                q = cur_q

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = list()
        if not root:
            return res
        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])
        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                res.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + "->" + str(node.left.val))
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + "->" + str(node.right.val))
        return res

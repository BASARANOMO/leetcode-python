# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])
        while queue1 and queue2:
            n1 = queue1.popleft()
            n2 = queue2.popleft()
            if n1.val != n2.val:
                return False
            left1, right1 = n1.left, n1.right
            left2, right2 = n2.left, n2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
                queue2.append(left2)
            if right1:
                queue1.append(right1)
                queue2.append(right2)
        return not queue1 and not queue2

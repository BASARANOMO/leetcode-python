# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, maxSum = 1, root.val
        level, q = 1, [root]
        while q:
            cur_sum, cur_q = 0, []
            for node in q:
                cur_sum += node.val
                if node.left:
                    cur_q.append(node.left)
                if node.right:
                    cur_q.append(node.right)
            if cur_sum > maxSum:
                maxSum = cur_sum
                ans = level
            q = cur_q
            level += 1
        return ans

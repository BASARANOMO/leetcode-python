# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            sumVal = node.val + dfs(node.left) + dfs(node.right)
            cnt[sumVal] += 1
            return sumVal
        
        dfs(root)
        maxCnt = max(cnt.values())
        return [key for key, value in cnt.items() if value == maxCnt]
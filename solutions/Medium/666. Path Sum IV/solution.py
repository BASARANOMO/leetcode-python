class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # hash
        tree_map = dict()
        sumList = list()
        for num in nums:
            tree_map[num // 10] = num % 10

        def dfs(pos: int, curSum: int) -> None:
            if pos not in tree_map:
                return
            curSum += tree_map[pos]
            curDepth = pos // 10
            curLevelPos = pos % 10
            leftPos = (curDepth + 1) * 10 + curLevelPos * 2 - 1
            rightPos = leftPos + 1
            if leftPos not in tree_map and rightPos not in tree_map:
                sumList.append(curSum)
            else:
                dfs(leftPos, curSum)
                dfs(rightPos, curSum)

        dfs(11, 0)
        return sum(sumList)

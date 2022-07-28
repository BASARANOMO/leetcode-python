class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_order_map = {val: idx for idx, val in enumerate(sorted(set(arr)), 1)} # Start from the specified index 1
        return [sorted_order_map[val] for val in arr]
        
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_order_map = dict()
        arr_sorted = sorted(arr)
        n = len(arr)
        last_val = 0
        last_order = 1
        for i in range(n):
            if last_val != arr_sorted[i]:
                last_val = arr_sorted[i]
                sorted_order_map[last_val] = last_order
                last_order += 1
        for i in range(n):
            arr[i] = sorted_order_map[arr[i]]
        return arr

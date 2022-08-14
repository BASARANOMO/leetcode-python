class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mntn_stk = [(prices[0], 0)]
        n = len(prices)
        i = 1
        while i < n:
            cur_val = prices[i]
            while mntn_stk and cur_val <= mntn_stk[-1][0]:
                p, idx = mntn_stk.pop()
                prices[idx] = p - cur_val
            mntn_stk.append((prices[i], i))
            i += 1
        return prices

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - b_price)
            b_price = min(b_price, prices[i])
        return res
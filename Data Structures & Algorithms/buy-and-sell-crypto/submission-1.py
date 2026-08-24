class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res, p_buy = 0, p[0]
        for i in range(1, len(p)):
            if p[i] < p_buy: p_buy = p[i]
            else: res = max(res, p[i] - p_buy)
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_ = prices[0]
        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            res = max(res, prices[i] - min_)
        
        return res
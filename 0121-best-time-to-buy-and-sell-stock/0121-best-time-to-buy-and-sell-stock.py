class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_ = prices[0]
        for i in range(len(prices)):
            if min_ > prices[i]:
                min_ = prices[i]
            res = max(res, prices[i] - min_)
        
        return res
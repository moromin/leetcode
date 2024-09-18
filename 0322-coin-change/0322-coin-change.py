class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 10000000
        res = [MAX for _ in range(amount + 1)]
        res[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], res[i - coin] + 1)
        
        return -1 if res[amount] == MAX else res[amount]
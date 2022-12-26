class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf for _ in range(n + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            num = 1
            while num * num <= i:
                dp[i] = min(dp[i - num * num] + 1, dp[i])
                num += 1

        return dp[n]
                
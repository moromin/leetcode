class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0 for _ in range(N + 1)]
        dp[1] = cost[0]
        for i in range(2, N + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        return min(dp[N], dp[N - 1])
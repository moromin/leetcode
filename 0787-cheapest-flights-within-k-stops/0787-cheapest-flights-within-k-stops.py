class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[math.inf for _ in range(n)] for _ in range(k + 2)]
        
        for i in range(k+2):
            dp[i][src] = 0
        
        for i in range(1, k+2):
            for cur, next, price in flights:
                if dp[i-1][cur] != math.inf:
                    dp[i][next] = min(dp[i][next], dp[i - 1][cur] + price)
            # print(dp)
        
        return dp[k+1][dst] if dp[k+1][dst] != math.inf else -1
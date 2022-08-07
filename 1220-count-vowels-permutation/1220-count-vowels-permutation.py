from collections import Counter

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        MOD = 10 ** 9 + 7
        
        for i in range(5):
            dp[1][i] = 1;
        
        for i in range(1, n):
            dp[i + 1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % MOD
            dp[i + 1][1] = (dp[i][0] + dp[i][2]) % MOD
            dp[i + 1][2] = (dp[i][1] + dp[i][3]) % MOD
            dp[i + 1][3] = dp[i][2] % MOD
            dp[i + 1][4] = (dp[i][2] + dp[i][3]) % MOD
        
        res = 0
        for i in range(5):
            res = (res + dp[n][i]) % MOD
        # print(sum(dp[n]))
        return res
            
        
        
        
        
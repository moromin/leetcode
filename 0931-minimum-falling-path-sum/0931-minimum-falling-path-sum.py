class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [[math.inf for _ in range(N)] for _ in range(N)]
        dp[0] = matrix[0]
        for i in range(1, N):
            for j in range(N):
                for col in range(j-1, j+2):
                    if 0 <= col < N:
                        dp[i][j] = min(dp[i][j], dp[i - 1][col])
                dp[i][j] += matrix[i][j]
        return min(dp[N-1])
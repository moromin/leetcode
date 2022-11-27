class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        freshCount = 0
        N, M = len(grid), len(grid[0])
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.appendleft((i, j))
        
        while q and freshCount:
            for _ in range(len(q)):
                i, j = q.pop()
                for ni, nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 1:
                        freshCount -= 1
                        grid[ni][nj] = 2
                        q.appendleft((ni, nj))
            count += 1
        
        return count if not freshCount else -1
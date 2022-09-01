class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        def dfs(i, j):
            if rooms[i][j] == -1:
                return
            
            for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] != -1 and rooms[ni][nj] > rooms[i][j] + 1:
                    rooms[ni][nj] = rooms[i][j] + 1
                    dfs(ni, nj)
            
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j)
        
        
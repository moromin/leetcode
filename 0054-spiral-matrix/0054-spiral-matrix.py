class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        di, dj = 0, 1
        i, j = 0, 0
        n, m = len(matrix), len(matrix[0])
        SEEN = -1000
        
        for _ in range(n * m):
            res.append(matrix[i][j])
            matrix[i][j] = SEEN
            
            if i + di == n or j + dj == m or matrix[i + di][j + dj] == SEEN:
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) -> ...
                di, dj = dj, -di
            
            i += di
            j += dj
            # print(i, j, di, dj, res)
        
        return res
        
        
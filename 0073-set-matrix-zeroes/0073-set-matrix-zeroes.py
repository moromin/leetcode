class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = set()
        rows = set()
        
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n) :
                if matrix[row][col] == 0:
                    columns.add(col)
                    rows.add(row)
                    
        for row in range(m):
            for col in range(n) :
                if row in rows or col in columns:
                    matrix[row][col] = 0
        
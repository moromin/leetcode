class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        n, m = len(board), len(board[0])
        edges = [ij for k in range(max(n, m)) for ij in ((0, k), (n-1, k), (k, 0), (k, m-1))]
        
        while edges:
            i, j = edges.pop()
            if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                board[i][j] = '*'
                edges += [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        
        board[:] = [['XO'[c == '*'] for c in row] for row in board]
                
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows and columns
        for i in range(9):
            row = board[i]
            col = [board[j][i] for j in range(9)]
            if not self.isValidLine(row) or not self.isValidLine(col):
                return False
        
        # Validate sub-squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = []
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            square.append(board[i][j])
                if len(square) != len(set(square)):
                    return False
        
        return True
    
    def isValidLine(self, line):
        tmp = list(filter(lambda a: a != '.', line))
        return len(tmp) == len(set(tmp))
        
#     def printBoard(self, board):
#         for row in board:
#             print(row)
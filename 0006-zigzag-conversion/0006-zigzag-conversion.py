class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        lines = [[] for _ in range(numRows)]
        diff = 1
        row = 0
        for c in s:
            if row == 0:
                diff = 1
            elif row == numRows - 1:
                diff = -1
            
            lines[row].append(c)
            row += diff
        
        return "".join("".join(line) for line in lines)
        
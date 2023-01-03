class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        n = len(strs[0])
        count = 0
        for i in range(n):
            for row in range(1, rows):
                if ord(strs[row - 1][i]) > ord(strs[row][i]):
                    count += 1
                    break
        return count
            
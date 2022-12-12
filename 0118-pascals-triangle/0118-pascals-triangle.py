class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            tmp = [1] * i
            for j in range(1, i - 1):
                tmp[j] = res[i-2][j-1] + res[i-2][j]
            res.append(tmp)
        return res
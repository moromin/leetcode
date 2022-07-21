class Solution:
    def integerBreak(self, n: int) -> int:
        
        def split(num, sp):
            if sp == 1:
                return num
            res = num // sp
            return res * split(num - res, sp - 1)
        
        res = 0
        for i in range(2, n+1):
            res = max(res, split(n, i))
            # print(res)
        
        return res
        
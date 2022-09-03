class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        
        def dfs(n, sums, num):
            if num < 0 or 9 < num :
                return
            if n == 0:
                res.add(sums)
                return
            sums *= 10
            sums += num
            dfs(n - 1, sums, num - k)
            dfs(n - 1, sums, num + k)
        
        for i in range(1, 10):
            dfs(n, 0, i)
        
        return list(res)
            
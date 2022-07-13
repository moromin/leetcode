class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        
        def dfs(node, idx):
            seen.add(idx)
            for i, elem in enumerate(node):
                if elem == 1 and i not in seen:
                    dfs(isConnected[i], i)
        
        res = 0
        for i in range(len(isConnected)):
            if i in seen:
                continue
            dfs(isConnected[i], i)
            # print(seen)
            res += 1
        
        return res
            
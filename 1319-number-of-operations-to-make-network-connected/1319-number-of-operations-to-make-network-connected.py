class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        visited = set()
        connected = 0
        
        d = collections.defaultdict(list)
        for i, j in connections:
            d[i].append(j)
            d[j].append(i)
        
        def dfs(conn):
            visited.add(conn)
            for c in d[conn]:
                if c not in visited:
                    dfs(c)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
            
        return connected - 1
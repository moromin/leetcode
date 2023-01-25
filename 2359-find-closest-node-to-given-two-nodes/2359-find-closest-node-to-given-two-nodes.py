class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        
        n = len(edges)
        routes1 = [-1 for _ in range(n)]
        routes2 = [-1 for _ in range(n)]
        def dfs(routes, node):
            dist = 0
            while node != -1 and routes[node] == -1:
                routes[node] = dist
                dist += 1
                node = edges[node]
        
        dfs(routes1, node1)
        dfs(routes2, node2)
    
        res = -1
        minLen = inf
        for i in range(n):
            if min(routes1[i], routes2[i]) >= 0 and max(routes1[i], routes2[i]) < minLen:
                minLen = max(routes1[i], routes2[i])
                res = i
            
        return res
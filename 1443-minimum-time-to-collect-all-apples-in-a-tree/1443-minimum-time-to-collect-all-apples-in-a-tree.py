class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            total = 0
            for child in graph[node]:
                total += dfs(child)
            if total > 0:
                return total + 2
            return 2 if hasApple[node] else 0
            
        return max(dfs(0) - 2, 0)
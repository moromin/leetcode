class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [0 for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        
        def dfs(num):
            counter = Counter()
            if num in visited:
                return counter
            visited.add(num)
            counter = Counter(labels[num])
            for child in graph[num]:
                counter += dfs(child)
            res[num] = counter[labels[num]]
            return counter
        dfs(0)
        
        return res
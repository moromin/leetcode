class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        m = defaultdict(list)
        for u, v in edges:
            m[u].append(v)
            m[v].append(u)
        
        seen = set()
        q = deque()
        q.appendleft(source)
        while q:
            node = q.pop()
            seen.add(node)
            if node == destination:
                return True
            for n in m[node]:
                if n not in seen:
                    q.appendleft(n)
        return False
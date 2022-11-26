class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = [(0, k)]
        ts = {}
        nodes = defaultdict(list)
        
        for u, v, w in times:
            nodes[u].append((v, w))
        
        while q:
            # print(q)
            time, node = heapq.heappop(q)
            if node not in ts:
                ts[node] = time
                for v, w in nodes[node]:
                    heapq.heappush(q, (time + w, v))
        return max(ts.values()) if len(ts) == n else -1
        
        
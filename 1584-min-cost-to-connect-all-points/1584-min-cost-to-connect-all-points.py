class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = defaultdict(list)
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                nodes[i].append((d, j))
                nodes[j].append((d, i))
                
        seen = set()
        res = 0
        count = 1
        q = nodes[0]
        seen.add(0)
        heapq.heapify(q)
        while q:
            d, j = heapq.heappop(q)
            if j not in seen:
                seen.add(j)
                count += 1
                res += d
                for record in nodes[j]:
                    heapq.heappush(q, record)
            if count >= N:
                break
        return res
            
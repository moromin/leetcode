class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def calcSlope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x2 - x1 == 0:
                return inf
            return (y2 - y1) / (x2 - x1)
        
        n = len(points)
        res = -inf
        for i in range(n):
            d = defaultdict(int)
            for j in range(i+1, n):
                slope = calcSlope(points[i], points[j])
                d[slope] += 1
                res = max(res, d[slope])
                # print(d)
        
        return res + 1
        
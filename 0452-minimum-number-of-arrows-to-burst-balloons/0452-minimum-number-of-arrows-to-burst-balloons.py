class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = []
        res.append(points[0])

        for i in range(1, len(points)):
            point = points[i]
            if point[0] <= res[-1][1]:
                res[-1][0] = point[0]
                res[-1][1] = min(res[-1][1], point[1])
            else:
                res.append(point)
        return len(res)
            
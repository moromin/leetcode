class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        intervals.sort()
        res = []
        i = 1
        preStart, preEnd = intervals[0]
        res.append(intervals[0])
        while i < N:
            if intervals[i][0] <= preEnd:
                preEnd = max(intervals[i][1], preEnd)
                res[-1][1] = preEnd
            else:
                res.append(intervals[i])
                preEnd = intervals[i][1]
            i += 1
        return res
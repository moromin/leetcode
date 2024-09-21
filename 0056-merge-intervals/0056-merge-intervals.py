class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        
        for s, e in intervals:
            if end < s:
                res.append([start, end])
                start = s
            end = max(e, end)
        
        if not res or res[-1] != [start, end]:
            res.append([start, end])
        return res
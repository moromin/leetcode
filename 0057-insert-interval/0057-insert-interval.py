class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        newStart, newEnd = newInterval[0], newInterval[1]
        inserted = False
        
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            
            if newEnd < start and not inserted:
                res.append([newStart, newEnd])
                inserted = True
            
            if start <= newStart <= end:
                newStart = start
            if start <= newEnd <= end:
                newEnd = end
            
            if not newStart <= start <= end <= newEnd: 
                res.append(intervals[i])
        
        if not inserted:
            res.append([newStart, newEnd])
        
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        if N == 0:
            return [newInterval]
        
        res = []
        i = 0
        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        newStart, newEnd = newInterval[0], newInterval[1] 
        while i < N and intervals[i][0] <= newInterval[1]:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1    
        res.append([newStart, newEnd])

        while i < N:
            res.append(intervals[i])
            i += 1
        
        return res
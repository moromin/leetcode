class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        count = 1
        end = intervals[0][1]
        for i in range(1, N):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return N - count
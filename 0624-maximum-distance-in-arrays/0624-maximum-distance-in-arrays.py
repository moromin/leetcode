class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            array = arrays[i]
            res = max(res, abs(array[-1] - smallest), abs(biggest - array[0]))
            smallest = min(smallest, array[0])
            biggest = max(biggest, array[-1])
        
        return res
            
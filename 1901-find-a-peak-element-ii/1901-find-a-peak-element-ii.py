from collections import Counter

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def findPeakIndex(nums) -> int:
            m, idx = nums[0], 0
            for i in range(len(nums)):
                if m < nums[i]:
                    m = nums[i]
                    idx = i
            return idx
        
        m, n = len(mat), len(mat[0])
        
        i = j = 0
        while True:
            preI, preJ = i, j
            j = findPeakIndex(mat[i])
            i = findPeakIndex([mat[i][j] for i in range(m)])
            if preI == i and preJ == j:
                break
                
        return [i, j]    

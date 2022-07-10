class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        m = -math.inf
        res = (0, m)
        for i, num in enumerate(nums):
            if num > m:
                m = num
                res = (i, m)
        
        return res[0]
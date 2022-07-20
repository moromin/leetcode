class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if nums is None or len(nums) <= 2:
            return 0
        
        start, end = 0, 2
        res = 0
        while end < len(nums):
            if nums[end] - nums[end - 1] == nums[end - 1] - nums[end - 2]:
                end += 1
            else:
                end += 1
                start = end - 2
            res += (end - start - 2)
            
        return res
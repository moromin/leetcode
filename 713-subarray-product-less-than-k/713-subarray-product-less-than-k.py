from collections import deque

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        left = res = 0
        for right in range(len(nums)):
            prod *= nums[right]
            
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            
            res += right - left + 1
            # print(left, right, res)
                
        return res
            
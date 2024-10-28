class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1 for i in range(n + 1)]
        right = [1 for i in range(n + 1)]
        
        for i in range(n):
            left[i + 1] = left[i] * nums[i]
            right[n - i - 1] = right[n - i] * nums[n - i - 1]
        
        res = []
        for i in range(n):
            res.append(left[i] * right[i + 1])
        
        return res
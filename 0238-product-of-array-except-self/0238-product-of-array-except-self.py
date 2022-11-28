class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1 for _ in range(N)]
        right = [1 for _ in range(N)]
        
        #       [1, 2, 3, 4]
        # left: [1, 1, 2, 6]
        # right:[24,12,4, 1]
        for i in range(1, N):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(N - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        return [left[i] * right[i] for i in range(N)]
         
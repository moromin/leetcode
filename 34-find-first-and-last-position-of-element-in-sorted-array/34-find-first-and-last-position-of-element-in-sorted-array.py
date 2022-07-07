class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        n = len(nums)
        
        def binarySearch(left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1
        
        start = binarySearch(0, n)
        if start == -1:
            return [-1, -1]
        while start - 1 >= 0 and nums[start - 1] == target:
            start -= 1
        
        end = binarySearch(start, n)
        while end + 1 < n and nums[end + 1] == target:
            end += 1
        
        return [start, end]
            
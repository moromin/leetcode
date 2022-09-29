class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif arr[-1] <= x:
            return arr[-k:]
        
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        return arr[left:right+1]
        
        
                
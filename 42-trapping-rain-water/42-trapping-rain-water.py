class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        maxLeft = maxRight = 0
        res = 0
        
        while left <= right:
            if heights[left] <= heights[right]:
                if heights[left] >= maxLeft:
                    maxLeft = heights[left]
                else:
                    res += maxLeft - heights[left]
                left += 1
            else:
                if heights[right] >= maxRight:
                    maxRight = heights[right]
                else:
                    res += maxRight - heights[right]
                right -= 1
            # print(left, right, res)
        return res
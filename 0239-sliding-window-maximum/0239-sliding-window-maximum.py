from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for i in range(k):
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
        res.append(d[0])

        for i in range(k, len(nums)):
            if d and d[0] == nums[i - k]:
                d.popleft()
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
            res.append(d[0])

        return res
        
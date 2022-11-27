class Solution:
    def rob(self, nums: List[int]) -> int:      
        pre, cur = 0, 0
        for i in nums:
            pre, cur = cur, max(pre + i, cur)
            # print(pre, cur)
        return cur
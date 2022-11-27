from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        
        def comb(elem, idx):
            res.append(elem)
            if idx == N:
                return
            for i in range(idx, N):
                comb(elem + [nums[i]], i + 1)
        
        comb([], 0)
        return res
        
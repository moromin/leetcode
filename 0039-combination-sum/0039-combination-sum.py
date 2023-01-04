class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def combination(nums, tmp, sums):
            if sums >= target:
                if sums == target:
                    res.append(tmp.copy())
                return
            for i, num in enumerate(nums):
                combination(nums[i:], tmp + [num], sums + num)
        
        combination(candidates, [], 0)
        return list(res)
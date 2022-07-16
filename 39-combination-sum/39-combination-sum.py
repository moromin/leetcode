class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None:
            return []
        
        res = []
        
        def combination(nums, comb, target):
            # print(comb, target)
            if target == 0:
                res.append(comb)
                return
            elif target < 0:
                return
            
            for i, c in enumerate(nums):
                combination(nums[i:], comb + [c], target - c)
                
        
        combination(candidates, [], target)
        return res
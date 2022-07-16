class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(nums, path):
            # print(path)
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[:i] + nums[i+1:], path+[nums[i]])
        
        dfs(nums, [])
        
        return res
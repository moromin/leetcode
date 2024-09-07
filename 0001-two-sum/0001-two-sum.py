class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = [(nums[i], i) for i in range(len(nums))]
        ns.sort()
        
        start, end = 0, len(ns) - 1
        
        while True:
            if ns[start][0] + ns[end][0] == target:
                return [ns[start][1], ns[end][1]]
            elif ns[start][0] + ns[end][0] < target:
                start += 1
            else:
                end -= 1
        
        return [0, 1]
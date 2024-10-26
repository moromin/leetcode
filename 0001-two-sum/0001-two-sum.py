class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        indexedNums = [(nums[i], i) for i in range(l)]
        indexedNums.sort()

        left, right = 0, l - 1
        while True:
            n1, i = indexedNums[left]
            n2, j = indexedNums[right]
            
            if n1 + n2 == target:
                return [i, j]
            elif n1 + n2 < target:
                left += 1
            else:
                right -= 1
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            ans += 1
            print(lastIdx, nextIdx)
            lastIdx, nextIdx = nextIdx, max(i + nums[i] for i in range(lastIdx, nextIdx + 1))
            print(lastIdx, nextIdx)
            print('---------------')
        return ans
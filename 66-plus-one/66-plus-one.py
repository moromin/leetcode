class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
# recursive
#         n = len(digits)
#         def traverse(idx) -> bool:
#             if idx == n - 1:
#                 res = digits[idx] + 1
#                 digits[idx] = res % 10
#                 return res // 10 == 1
            
#             res = digits[idx]
#             if traverse(idx+1):
#                 res += 1
#             digits[idx] = res % 10
#             return res // 10 == 1
            
#         if traverse(0):
#             digits = [1] + digits
#         return digits
            
                
# simple
        sums = 0
        for d in digits:
            sums = d + sums * 10
        sums += 1
        res = collections.deque()
        while sums:
            res.appendleft(sums % 10)
            sums //= 10
        return list(res)
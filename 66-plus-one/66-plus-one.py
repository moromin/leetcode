class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        def traverse(idx) -> bool:
            if idx == n - 1:
                res = digits[idx] + 1
                digits[idx] = res % 10
                return res // 10 == 1
            
            res = digits[idx]
            if traverse(idx+1):
                res += 1
            digits[idx] = res % 10
            return res // 10 == 1
            
        if traverse(0):
            digits = [1] + digits
        return digits
            
                
        
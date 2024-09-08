class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            
            a = sum
            b = carry
        
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        num = 1
        while num < n:
            num <<= 2
        
        return num == n
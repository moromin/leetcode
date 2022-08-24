class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = 1
        while n > x:
            x *= 3
        
        return n == x
        
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        SP = {
            'I': ['X', 'V'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        
        res = 0
        
        for i in range(len(s)):
            if s[i] in ('I', 'X', 'C') and i + 1 < len(s):
                if s[i + 1] in SP[s[i]]:
                    res -= ROMAN[s[i]]
                    continue
            res += ROMAN[s[i]]
        
        return res
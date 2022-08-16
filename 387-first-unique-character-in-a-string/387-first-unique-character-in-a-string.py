from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
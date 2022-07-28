from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m1 = defaultdict(int)
        for _, c in enumerate(s):
            m1[c] += 1
        
        m2 = defaultdict(int)
        for _, c in enumerate(t):
            m2[c] += 1
            
        for _, k in enumerate(m1):
            # print(k, m1[k])
            if k not in m2 or m1[k] != m2[k]:
                return False
        
        return True
from collections import defaultdict 

class Solution:
    def buildMap(self, s):
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        return m
        
    def isAnagram(self, s: str, t: str) -> bool:
        sm = self.buildMap(s)
        tm = self.buildMap(t)
        
        return sm == tm
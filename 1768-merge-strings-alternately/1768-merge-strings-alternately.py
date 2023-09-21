class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        
        i = j = 0
        res = ""
        while i < n or j < m:
            if i < n:
                res += word1[i]
                i += 1
            if j < m:
                res += word2[j]
                j += 1
        return res
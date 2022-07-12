class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pm = defaultdict(int)
        window = defaultdict(int)
        
        for c in p:
            pm[c] += 1
        
        for i in range(len(s)):
            if i >= len(p) and s[i - len(p)] in pm:
                window[s[i-len(p)]] -= 1
                
            if s[i] in pm:
                window[s[i]] += 1
                if window == pm:
                    res.append(i - len(p) + 1)
                
        return res
            
            
                
            
                
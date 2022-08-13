class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        
        n, cnt = len(s), len(words)
        if n <= 0 or cnt <= 0:
            return res
        
        wl = len(words[0])
        d = {}
        for _, word in enumerate(words):
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        i = 0
        for k in range(wl):
            left, count = k, 0
            subd = {}
            for j in range(k, n - wl + 1, wl):
                tword = s[j:j+wl]
                
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+wl]] -= 1
                        left += wl
                        count -= 1
                    if count == cnt:
                        res.append(left)
                
                # invalid word
                else:
                    left = j + wl
                    subd = {}
                    count = 0
        return res
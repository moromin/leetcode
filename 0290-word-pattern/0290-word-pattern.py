class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p2w = dict()
        w2p = dict()
        n = len(pattern)
        if n != len(words):
            return False
        
        for i in range(n):
            key = pattern[i]
            word = words[i]
            if key not in p2w:
                if word in w2p:
                    return False
                p2w[key] = word
                w2p[word] = key
            else:
                if word != p2w[key]:
                    return False
        return True
                
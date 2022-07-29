class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if len(pattern) == 0 or words is None or len(words) == 0:
            return []
        
        def hash(word):
            res = 0
            diff = 0
            m = dict()
            for i in range(len(word)):
                if word[i] not in m:
                    diff += 1
                    m[word[i]] = diff
                res = m[word[i]] + res * 10
            return res
        
        res = []
        patternHash = hash(pattern)
        for word in words:
            wordHash = hash(word)
            if wordHash == patternHash:
                res.append(word)
        
        return res
        
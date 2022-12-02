class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if len(c1) != len(c2):
            return False
        
        n = len(word1)
        s1 = set()
        s2 = set()
        fre1 = []
        fre2 = []

        for w, count in c1.most_common():
            s1.add(w)
            fre1.append(count)
        for w, count in c2.most_common():
            s2.add(w)
            fre2.append(count)
        
        return s1 == s2 and fre1 == fre2

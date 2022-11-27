class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter([])
        for i in range(m):
            c2.subtract(Counter({s2[i]:-1}))
            if i >= n:
                c2.subtract(Counter({s2[i - n]:1}))
            if c1 == c2:
                return True
        return False
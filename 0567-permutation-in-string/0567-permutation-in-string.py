class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = [0 for _ in range(26)]
        window = [0 for _ in range(26)]
        for c in s1:
            pattern[ord(c) - ord('a')] += 1
        n = len(s1)
        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            if i >= n:
                window[ord(s2[i - n]) - ord('a')] -= 1
            if window == pattern:
                return True
        return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = [0 for _ in range(26)]
        word = [0 for _ in range(26)]
        for c in s1:
            window[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            word[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                word[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if word == window:
                return True
        return False
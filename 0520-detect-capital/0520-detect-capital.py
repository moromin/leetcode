class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first = ord('A') <= ord(word[0]) <= ord('Z')
        word = word[1:]
        upper = word.isupper()
        lower = word.islower()
        return (not first and lower) or (first and (upper or lower))
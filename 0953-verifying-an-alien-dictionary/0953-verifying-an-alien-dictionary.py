class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {order[i]: i for i in range(len(order))}
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]) and words[i][j] == words[i + 1][j]:
                j += 1
            if j == len(words[i]):
                continue
            if j == len(words[i + 1]) or order[words[i][j]] > order[words[i+1][j]]:
                return False
        return True
            
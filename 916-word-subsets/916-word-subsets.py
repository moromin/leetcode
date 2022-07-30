from collections import Counter

class Solution:
#     Counter solution
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         count = Counter()
#         for word in words2:
#             count |= Counter(word)
        
#         return [word for word in words1 if not count - Counter(word)]
            
#   Map solution
    def wordSubsets(self, words1, words2):
        def count(word):
            ans = [0 for _ in range(26)]
            for c in word:
                ans[ord(c) - ord('a')] += 1
            return ans
    
        bmax = [0 for _ in range(26)]
        for word in words2:
            for i, c in enumerate(count(word)):
                bmax[i] = max(bmax[i], c)
        
        return [word for word in words1 if all(x >= y for x, y in zip(count(word), bmax))]
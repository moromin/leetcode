from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        
        res = 0
        sums = 0
        for _, count in c.most_common():
            res += 1
            sums += count
            if sums >= n // 2:
                break
        
        return res
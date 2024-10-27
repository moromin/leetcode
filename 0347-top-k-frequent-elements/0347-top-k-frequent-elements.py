from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        freqs = [(count, n) for n, count in m.items()]
        freqs.sort()
   
        return [n for c, n in freqs][-k:]
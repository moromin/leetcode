from collections import Counter

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        idx1 = idx2 = 0
        while idx1 < len(encoded1) and idx2 < len(encoded2):
            val1, freq1 = encoded1[idx1]
            val2, freq2 = encoded2[idx2]
            
            prod = val1 * val2
            freq = min(freq1, freq2)
            encoded1[idx1][1] -= freq
            encoded2[idx2][1] -= freq
            
            if encoded1[idx1][1] == 0:
                idx1 += 1
            if encoded2[idx2][1] == 0:
                idx2 += 1
            
            if not res or res[-1][0] != prod:
                res.append([prod, freq])
            else:
                res[-1][1] += freq
            # print(res)
            
        return res
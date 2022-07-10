class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if firstList is None or secondList is None \
            or len(firstList) == 0 or len(secondList) == 0:
                return []
            
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            if e1 < s2:
                i += 1
                continue
            elif e2 < s1:
                j += 1
                continue
                
            if e1 > e2:
                j += 1
            else:
                i += 1
            
            res.append([max(s1, s2), min(e1, e2)])
        
        return res
                
            
            
            
                
                
        
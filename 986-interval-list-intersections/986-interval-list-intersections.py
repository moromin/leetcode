class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList is None or secondList is None:
                return []
            
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            l, r = max(s1, s2), min(e1, e2)
            
            if l <= r:
                res.append([l, r])
                
            if e1 > e2:
                j += 1
            else:
                i += 1
        
        return res
                
            
            
            
                
                
        
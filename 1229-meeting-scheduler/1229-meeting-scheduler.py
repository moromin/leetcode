class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []
        
        slots1.sort()
        slots2.sort()
            
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            
            s, e = max(s1, s2), min(e1, e2)
            if e - s >= duration:
                return [s, s + duration]
            if e1 < e2:
                i += 1
            else:
                j += 1
        
        return []
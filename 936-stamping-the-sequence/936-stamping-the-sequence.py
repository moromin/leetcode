from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        options = {i*'*' + stamp[i:j] + (len(stamp) - j)*'*' for i in range(len(stamp)) for j in range(i, len(stamp) + 1)} - {'*'*len(stamp)}
        res = []
        target = list(target)
        
        updates = -1
        while updates:
            i = updates = 0
            t = ''.join(target)
            while i <= len(t) - len(stamp):
                if t[i:i+len(stamp)] in options:
                    res.append(i)
                    target[i:i+len(stamp)] = ['*'] * len(stamp)
                    updates += 1
                i += 1
        
        return res[::-1] if set(target) == {'*'} else []
            
        
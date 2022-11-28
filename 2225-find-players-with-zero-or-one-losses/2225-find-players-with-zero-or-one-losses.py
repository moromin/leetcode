class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        wins = defaultdict(int)
        keys = set()
        for w, l in matches:
            wins[w] += 1
            loses[l] += 1
            keys.add(w)
            keys.add(l)
        
        ws = []
        ls = []
        for key in sorted(list(keys)):
            if key in wins and key not in loses:
                ws.append(key)
            elif key in loses and loses[key] == 1:
                ls.append(key)
        return [ws, ls]
            
            
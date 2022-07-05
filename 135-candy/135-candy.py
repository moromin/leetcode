from collections import defaultdict

class Solution:
    def candy(self, ratings: List[int]) -> int:
        children = defaultdict(list)
        for i, r in enumerate(ratings):
            children[r].append(i)
            
        low, high = min(ratings), max(ratings)
        
        res = [0 for _ in range(len(ratings))]
        
        for r in range(low, high + 1):
            if r not in children:
                continue
    
            while children[r]:
                idx = children[r].pop()
                left = right = 1
                if idx - 1 >= 0 and ratings[idx - 1] < ratings[idx]:
                    left = res[idx - 1] + 1
                if idx + 1 < len(ratings) and ratings[idx] > ratings[idx + 1]:
                    right = res[idx + 1] + 1
                res[idx] = max(left, right)
        
        # print(res)
        return sum(res)
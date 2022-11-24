import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones = list(map(lambda x: x*(-1), stones)) 
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # print(stones)
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            
            if x == y:
                continue
            elif x < y:
                x, y = y, x
            heapq.heappush(stones, -(x - y))
            
        return -stones[0] if len(stones) == 1 else 0
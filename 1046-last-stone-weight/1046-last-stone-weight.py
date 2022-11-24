import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, x - y)
            
        return -stones[0] if len(stones) == 1 else 0
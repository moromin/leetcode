class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / mid)

            if count <= h:
                high = mid - 1
            else:
                low = mid + 1
        
        return low
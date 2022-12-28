class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        for i in range(n):
            capacity[i] -= rocks[i]
        capacity.sort()
        for i in range(n):
            if additionalRocks <= 0:
                break
            if capacity[i] > 0:
                additionalRocks -= capacity[i]
                if additionalRocks >= 0:
                    capacity[i] = 0

        return capacity.count(0)
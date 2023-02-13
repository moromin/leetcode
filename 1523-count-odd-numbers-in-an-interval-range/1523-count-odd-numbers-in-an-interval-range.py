class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        return count + 1 if low % 2 == 1 or high % 2 == 1 else count
        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = total = tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1
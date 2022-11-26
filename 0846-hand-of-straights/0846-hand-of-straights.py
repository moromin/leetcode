class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0:
            return False
        
        Min = hand[0]
        counter = defaultdict(int)
        s = set()
        for h in hand:
            s.add(h)
            counter[h] += 1
        
        INF = 1_000_000_000
        q = list(s)
        heapq.heapify(q)
        for g in range(N // groupSize):
            start = q[0]
            for i in range(start, start + groupSize):
                if i not in counter or counter[i] == 0:
                    return False
                counter[i] -= 1
                Min = min(Min, i)
                if counter[i] == 0:
                    heapq.heappop(q)
                
        return True
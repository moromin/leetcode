class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        
        res = 0
        for count in counter.values():
            while count:
                if count < 2:
                    return -1
                if count - 3 >= 2 or (count - 3) % 3 == 0:
                    count -= 3
                else:
                    count -= 2
                res += 1
        return res
            
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        Max = 0
        maxCount = 0
        for task in tasks:
            counter[task] += 1
            if Max == counter[task]:
                maxCount += 1
            elif Max < counter[task]:
                Max = counter[task]
                maxCount = 1
        
        partCount = Max - 1
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength
        availableTasks = len(tasks) - Max * maxCount
        idles = max(0, emptySlots - availableTasks)
        return len(tasks) + idles
        
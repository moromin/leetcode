class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        
        start = 0
        res = 0
        for i in range(len(fruits)):
            basket[fruits[i]] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            res = max(res, i - start + 1)
        
        return res
        
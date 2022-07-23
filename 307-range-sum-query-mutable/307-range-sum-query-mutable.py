class NumArray:
    def __init__(self, nums: List[int]):
        def add(x, y):
            return x + y
        
        n = len(nums)
        self.n = n
        self.e = 0
        self.op = add
        self.size = 1 << (n - 1).bit_length()
        self.d = [self.e] * (2 * self.size)
        for i in range(n):
            self.d[self.size + i] = nums[i]
        for i in range(self.size - 1, 0, -1):
            self.d[i] = self.op(self.d[2 * i], self.d[2 * i + 1])
    
    def update(self, index: int, val: int) -> None:
        assert 0 <= index < self.n
        
        index += self.size
        self.d[index] = val
        while index > 1:
            index >>= 1
            self.d[index] = self.op(self.d[2 * index], self.d[2 * index + 1])

    def sumRange(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= self.n
        
        sml = smr = self.e
        left += self.size
        right += self.size + 1
        
        while left < right:
            if left & 1:
                sml = self.op(sml, self.d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self.op(self.d[right], smr)
            left >>= 1
            right >>= 1
        return self.op(sml, smr)


# Your NumArray object will be instantiated and called as such:
# nums = [1, 3, 5]
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
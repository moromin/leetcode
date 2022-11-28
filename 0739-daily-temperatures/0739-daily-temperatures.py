class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        N = len(A)
        res = [0 for _ in range(N)]
        stack = deque()
        
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
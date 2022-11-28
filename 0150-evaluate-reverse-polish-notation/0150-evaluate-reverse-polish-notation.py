class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        def calc(x, y, token):
            if token == '+':
                return x + y
            elif token == '-':
                return x - y
            elif token == '/':
                res = x // y
                return res + 1 if x * y < 0 and x % y != 0 else res
            else:
                return x * y
        
        for token in tokens:
            if token in ('+', '-', '/', '*'):
                y = stack.pop()
                x = stack.pop()
                stack.append(calc(x, y, token))
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]
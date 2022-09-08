class Solution:
    def decodeString(self, s: str) -> str:
        curStr = ''
        curNum = 0
        stack = collections.deque()
        for c in s:
            if c == '[':
                stack.append((curStr, curNum))
                curStr = ''
                curNum = 0
            elif c == ']':
                preStr, num = stack.pop()
                curStr = preStr + num * curStr
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curStr += c
        return curStr
            
                
                
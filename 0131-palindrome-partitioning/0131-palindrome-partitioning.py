class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
    
        def backtrack(st, path):
            if not st:
                res.append(path)
            for i in range(1, len(st) + 1):
                if isPalindrome(st[:i]):
                    backtrack(st[i:], path+[st[:i]])
            
        res = []
        backtrack(s, [])
        return res
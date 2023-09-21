class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = count = 0
        
        n = len(s)
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                tmp = ""
                while i < n and s[i] != " ":
                    tmp += s[i]
                    i += 1
                if count != 0:
                    res = " " + res
                res = tmp + res
                count += 1
        return res
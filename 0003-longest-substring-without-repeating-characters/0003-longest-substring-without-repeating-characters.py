class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         max_len = 0
        
#         tmp = ''
#         for i in range(n):
#             while s[i] in tmp:
#                 tmp = tmp[1:]
#             tmp += s[i]
#             print(tmp)
#             max_len = max(max_len, len(tmp))
        
#         return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        pos = {s[i]: -1 for i in range(N)}
        
        start = 0
        res = 0
        for i in range(N):
            if pos[s[i]] >= start:
                start = pos[s[i]] + 1
            pos[s[i]] = i
            res = max(res, i - start + 1)
            # print(i, start, pos)
        return res

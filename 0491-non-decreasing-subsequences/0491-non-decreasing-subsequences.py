class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursive(tmp, nl):
            if len(tmp) >= 2 and tmp not in res:
                res.append(tmp.copy())
            # print(tmp, nl, res)
            if not nl:
                return
            for i in range(len(nl)):
                if not tmp or tmp[-1] <= nl[i]:
                    tmp.append(nl[i])
                    recursive(tmp, nl[i+1:])
                    tmp.pop()
        recursive([], nums)
        return res
                    
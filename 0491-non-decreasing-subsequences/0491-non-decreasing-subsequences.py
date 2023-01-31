class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def recursive(tmp, nl):
            if len(tmp) >= 2:
                res.add(tuple(tmp))
            # print(tmp, nl, res)
            if not nl:
                return
            for i in range(len(nl)):
                if not tmp or tmp[-1] <= nl[i]:
                    tmp.append(nl[i])
                    recursive(tmp, nl[i+1:])
                    tmp.pop()
        recursive([], nums)
        return list(res)
                    
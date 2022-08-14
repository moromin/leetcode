from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or beginWord == endWord or not beginWord or not endWord or not wordList:
            return []
        
        n = len(beginWord)
        
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        # build graph, bi-BFS
        bq = deque()
        bq.append(beginWord)
        eq = deque()
        eq.append(endWord)
        bvisited = set([beginWord])
        evisited = set([endWord])
        rev = False
        
        # graph
        parents = defaultdict(set)
        found = False
        depth = 0
        while bq and not found:
            depth += 1
            # print(bq)
            localVisited = set()
            for _ in range(len(bq)):
                word = bq.popleft()
                for i in range(n):
                    for nextWord in all_combo_dict[word[:i] + '*' + word[i+1:]]:
                        if nextWord == word:
                            continue
                        if nextWord not in bvisited:
                            if not rev:
                                parents[nextWord].add(word)
                            else:
                                parents[word].add(nextWord)
                            if nextWord in evisited:
                                found = True
                            localVisited.add(nextWord)
                            bq.append(nextWord)
            bvisited = bvisited.union(localVisited)
            bq, bvisited, eq, evisited, rev = eq, evisited, bq, bvisited, not rev
        
        res = []
        def dfs(node, path, d):
            # print(node, path)
            if d == 0:
                if path[-1] == beginWord:
                    res.append(path[::-1])
                return
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d - 1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return res
        
            
        
            
                    
        
                
        
        
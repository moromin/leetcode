from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for end, start in prerequisites:
            graph[start].append(end)
            degree[end] += 1
            
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for start in bfs:
            for end in graph[start]:
                degree[end] -= 1
                if degree[end] == 0:
                    bfs.append(end)
            
        return len(bfs) == numCourses
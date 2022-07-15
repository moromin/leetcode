class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph) - 1
        
        def bfs(road, i):
            if road[-1] == end:
                res.append(road.copy())
                return
            elif len(graph[i]) == 0:
                return
            
            for node in graph[i]:
                road.append(node)
                bfs(road, node)
                road.pop()
                
        bfs([0], 0)
        
        return res
        
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
        
        def bfs(q):
            visited = set()
            q = collections.deque(q)
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        q.append((ni, nj))
            return visited
        
        return bfs(pacific) & bfs(atlantic)
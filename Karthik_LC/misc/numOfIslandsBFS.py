class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        visited = set()
        
        def bfs(r, c):
            q = collections.deque()

            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    rr, cc = row + dr, col + dc

                    if (rr in range(rows) and cc in range(cols) and grid[rr][cc] == "1" and (rr,cc) not in visited):
                        q.append((rr,cc))
                        visited.add((rr,cc))
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    islands += 1
        
        return islands

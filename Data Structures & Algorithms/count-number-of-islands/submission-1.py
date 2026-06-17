class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] != "1" or (row, col) in visited:
                    continue
                visited.add((row, col))
                dfs(row, col)  

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visited.add((r, c))
                    dfs(r, c)
                    islands += 1

        
        return islands

        
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            nonlocal res
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 0:
                return
            if r == ROWS - 1 and c == COLS - 1:
                res += 1
            
            grid[r][c] = 1
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
            
            grid[r][c] = 0
        
        dfs(0, 0)
        return res
        


            



            

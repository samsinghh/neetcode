class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        def search(r, c):
            nonlocal res
            grid[r][c] = -1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if grid[nr][nc] == 1:
                        search(nr, nc)
                    elif grid[nr][nc] == 0:
                        res += 1
                else:
                    res += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    search(i, j)
                    break
        return res


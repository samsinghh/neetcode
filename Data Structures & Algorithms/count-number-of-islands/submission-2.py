class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0
        def search(r, c):
            grid[r][c] = '0'

            for dr, dc in dirs:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == '1':
                    search(r+dr, c+dc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += 1
                    search(r, c)
        
        return res
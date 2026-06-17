class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, lastHeight):
            if min(r, c) < 0 or r == ROWS or c == COLS or heights[r][c] < lastHeight or (r, c) in visited:
                return
            
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc, visited, heights[r][c])
            
        
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS-1, atl, -1)
        
        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS-1, c, atl, -1)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res                    
        
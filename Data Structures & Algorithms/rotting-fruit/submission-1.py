class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        numFresh = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    
        if numFresh == 0:
            return 0
            
        time = 0
        while q:
            changed = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] != 1:
                        continue
                    
                    q.append((row, col))
                    grid[row][col] = 2
                    numFresh -= 1
                    changed = True
                    
            if changed:
                time += 1
        
        return time if numFresh == 0 else -1





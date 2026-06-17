class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numFresh = 0
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while numFresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    newr, newc = r + dr, c + dc
                    if 0 <= newr < ROWS and 0 <= newc < COLS and grid[newr][newc] == 1:
                        numFresh -= 1
                        grid[newr][newc] = 2
                        q.append((newr, newc))
            time += 1
        
        return time if numFresh == 0 else -1
        


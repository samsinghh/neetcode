class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        level = 1 
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row+dr, col + dc
                    if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or (r, c) in visited:
                        continue
                    visited.add((r, c))
                    q.append((r, c))
                    grid[r][c] = level
            level += 1
        

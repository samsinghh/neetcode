class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc
                    if min(newr, newc) < 0 or newr == ROWS or newc == COLS or (newr, newc) in visited or grid[newr][newc] == -1:
                        continue
                    q.append([newr, newc])
                    visited.add((newr, newc))
            dist += 1
        



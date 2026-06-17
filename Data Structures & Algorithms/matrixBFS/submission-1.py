class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(0, 0)])
        visited = set()
        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                visited.add((r, c))
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] != 0:
                        continue
                    q.append((row, col))
            length += 1
        return -1
             

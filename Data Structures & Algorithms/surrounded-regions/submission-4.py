class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1 and board[r][c] == 'O'):
                    q.append((r, c))
        
        
        while q:
            r, c = q.popleft()
            if board[r][c] == 'O':
                board[r][c] = 'F'

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if min(row, col) < 0 or row == ROWS or col == COLS:
                        continue
                    q.append((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'F':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        

                

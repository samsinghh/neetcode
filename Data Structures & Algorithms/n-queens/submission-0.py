class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n) ]
        columns = set()
        left_diagonals = set()
        right_diagonals = set()
        def dfs(row):
            if row == n:
                sol = [''.join(row) for row in board]
                res.append(sol)
                return
            
            for col in range(n):
                if col in columns or (row - col) in left_diagonals or (row + col) in right_diagonals:
                    continue
                
                board[row][col] = 'Q'
                columns.add(col)
                left_diagonals.add(row - col)
                right_diagonals.add(row + col)

                dfs(row + 1)

                board[row][col] = '.'
                columns.remove(col)
                left_diagonals.remove(row - col)
                right_diagonals.remove(row + col)
        
        dfs(0)

        return res
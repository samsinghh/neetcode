class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        col = set()
        posDiag = set()
        negDiag = set()

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(r):
            if r == n:
                ans = [''.join(row) for row in board]
                res.append(ans)
                return
            
            for c in range(n):
                if c not in col and (r+c) not in posDiag and (r-c) not in negDiag:
                    posDiag.add((r+c))
                    negDiag.add((r-c))
                    col.add(c)

                    board[r][c] = 'Q'
                    backtrack(r+1)
                    board[r][c] = '.'
                    posDiag.remove((r+c))
                    negDiag.remove((r-c))
                    col.remove(c)
        
        backtrack(0)
        return res
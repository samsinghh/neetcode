# do some sort of searching algorithm on the grid, keeping the 
# current letters we've visited as a string
# only add chars that are in the word obviously
# if len(our string) == len(word), return True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def search(r, c, i):
            if i == len(word)-1:
                return True
            board[r][c] = '#'
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == word[i+1]:
                    if search(nr, nc, i+1):
                        return True
            board[r][c] = word[i]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and search(i, j, 0):
                    return True
        return False            


        
    
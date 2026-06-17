class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            elements = [num for num in row if num != '.']
            if len(set(elements)) != len(elements):
                return False

        # Check columns
        for column in zip(*board):
            elements = [num for num in column if num != '.']
            if len(set(elements)) != len(elements):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [
                    board[x][y] 
                    for x in range(i, i + 3) 
                    for y in range(j, j + 3) 
                    if board[x][y] != '.'
                ]
                if len(set(sub_box)) != len(sub_box):
                    return False

        return True
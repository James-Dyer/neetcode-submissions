class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without duplicates.
        row_set = set()
        col_set = set()
        square_set = set()
        for i in range(9):
            for j in range(9):
                # row
                if board[i][j] in row_set:
                    return False
                if board[i][j] != '.':
                    row_set.add(board[i][j]) 

                # col
                if board[j][i] in col_set:
                    return False
                if board[j][i] != '.':
                    col_set.add(board[j][i])

                square_row, square_col = (i // 3) * 3, (i % 3) * 3
                sub_row, sub_col = j // 3, j % 3
                curr = board[square_row + sub_row][square_col + sub_col]
                if curr in square_set:
                    return False
                if curr != '.':
                    square_set.add(curr)
            row_set.clear()
            col_set.clear()
            square_set.clear()
        
        return True
        

        
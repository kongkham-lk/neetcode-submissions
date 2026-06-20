class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = [set() for _ in range(9)], [set() for _ in range(9)]
        cell = [[] for _ in range(3)]
        for i in range(3):
            cell[i] = [set() for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i]: return False
                    else: row[i].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col[i]: return False
                    else: col[i].add(board[j][i])
                if board[i][j] != ".":
                    if board[i][j] in cell[i//3][j//3]: return False
                    else: cell[i//3][j//3].add(board[i][j])
                # print()
        print(cell)
        return True

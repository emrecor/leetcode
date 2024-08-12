class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        for y in range(9):
            for i in range(9):
                if board[y][i] == ".":
                    continue
                if (board[y][i] in rows[y] or board[y][i] in cols[i] or board[y][i] in sqrs[(y//3,i//3)]):
                    return False
                rows[y].add(board[y][i])
                cols[i].add(board[y][i])
                sqrs[(y//3,i//3)].add(board[y][i])

        return True
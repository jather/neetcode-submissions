class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = {i:set() for i in range(0,9)}
        colSet = {i:set() for i in range(0,9)}
        squareSet = {i:set() for i in range(0,9)}
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rowSet[i]:
                    return False
                rowSet[i].add(num)
                if num in colSet[j]:
                    return False
                colSet[j].add(num)
                square = (i // 3) * 3 + (j // 3)
                if num in squareSet[square]:
                    return False
                squareSet[square].add(num)
        return True
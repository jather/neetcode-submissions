class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        found = False

        def backtrack(row, col, i):
            nonlocal found
            if word[i] != board[row][col]:
                return
            if i == len(word) - 1:
                found = True
                return
            seen.add((row, col))
            if not found and row > 0 and (row - 1, col) not in seen:
                backtrack(row - 1, col, i + 1)
            if not found and row < len(board) - 1 and (row + 1, col) not in seen:
                backtrack(row + 1, col, i + 1)
            if not found and col > 0 and (row, col - 1) not in seen:
                backtrack(row, col - 1, i + 1)
            if not found and col < len(board[row]) - 1 and (row, col + 1) not in seen:
                backtrack(row, col + 1, i + 1)
            seen.remove((row, col))

        for i in range(len(board)):
            j = 0
            while not found and j < len(board[i]):
                backtrack(i, j, 0)
                j += 1

        return found
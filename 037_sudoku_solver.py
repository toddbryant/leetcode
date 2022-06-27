"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

from typing import List
from typing import Dict

class Solution:
    LEGAL_MOVES = set("123456789")
    GRAPH = {}

    def __init__(self):
        # Initialize a dict GRAPH with squares connected to other squares
        self.GRAPH = {}
        for i in range(0,9):
            for j in range(0,9):
                row = [(i,x) for x in range(0,9)]
                col = [(x,j) for x in range(0,9)]
                box_index = self.getBoxIndex(i,j)
                box = [(x,y) for x in range(0,9) for y in range(0,9) if self.getBoxIndex(x,y)==box_index]

                self.GRAPH[(i,j)] = set(row) | set(col) | set(box) - set((i,j))

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        blank_squares = sum(1 for row in board for c in row if c==".")
        self.solveRecursive(board, blank_squares)


    def solveRecursive(self, board: List[List[str]], blank_squares: int) -> bool:
        # Strategy: always fill in forced moves
        # Then, proceed recursively with backtracking
        if blank_squares==0:
            return True

       
        # Collect legal guesses by square, prioritize squares with fewer guesses
        guesses_by_len = {n:dict() for n in range(1,10)}
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == ".":
                    guesses = self.getGuessesAtSquare(board, i, j)
                    if not guesses: # Reached an illegal dead end
                        return False
                    guesses_by_len[len(guesses)][(i,j)] = guesses

            
        # Recurse through guesses with backtracking
        for length in range(1,10):
            for square in guesses_by_len[length]:
                i, j = square
                for guess in guesses_by_len[length][square]:
                    board[i][j] = guess
                    if self.solveRecursive(board, blank_squares - 1):
                        return True
                    board[i][j] = "."
                # No legal guesses for this square worked, dead end
                return False

    def getGuessesAtSquare(self, board: List[List[str]], i: int, j: int) -> List[str]:
        return self.LEGAL_MOVES-set([board[square[0]][square[1]] for square in self.GRAPH[(i,j)]])-set(board[i][j])

    def getBoxIndex(self, i, j):                
        return 3 * (i // 3) + (j // 3)

if __name__ == '__main__':
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Solution().solveSudoku(board)


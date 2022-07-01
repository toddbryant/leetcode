"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""
from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # strategy--
        # place queen
        # eliminate connected squares
        # backtrack if stuck

        legal_squares = set((i,j) for i in range(0, n) for j in range(0, n))

        # compute connected squares
        connected_squares = {square: set() for square in legal_squares}
        for square in connected_squares:
            for i in range(1, n):
                new_squares = [
                    (square[0]+i, square[1]),
                    (square[0], square[1]+i),
                    (square[0]+i, square[1]+i),
                    (square[0]-i, square[1]-i),
                    (square[0]-i, square[1]+i),
                    (square[0]+i, square[1]-i)
                ]
                for sq in new_squares:
                    if 0 <= sq[0] < n and 0 <= sq[1] < n:
                        connected_squares[square].add(sq)

        results = []
        
        board = []
        for i in range(n):
            board.append(["."]*n)

        def backtrack(board, i):
            if i==n:
                results.append([''.join(row) for row in board])

            for j in range(0, n):
                square = (i,j)
                if square in legal_squares:
                    # Make move and mark all connected squares illegal
                    board[i][j] = "Q"
                    removed_squares = set()
                    for sq in connected_squares[square]:
                        try:
                            legal_squares.remove(sq)
                            removed_squares.add(sq)
                        except KeyError:
                            pass
                    
                    backtrack(board, i+1)

                    # We've backtracked, undo the move
                    board[i][j] = "."
                    for sq in removed_squares:
                        legal_squares.add(sq)


        backtrack(board, 0)
        return results

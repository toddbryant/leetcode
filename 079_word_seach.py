"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_legal(i, j):
            return i>=0 and i<len(board) and j>=0 and j<len(board[0])
        
        def search(i, j, target):
            if not target:
                return True
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if is_legal(new_i, new_j) and board[new_i][new_j]==target[0]:
                    board[new_i][new_j] = '#'
                    if search(new_i, new_j, target[1:]):
                        return True
                    board[new_i][new_j] = target[0]
            return False
                        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if board[i][j]==word[0]:
                    board[i][j] = '#'
                    if search(i, j, word[1:]):
                        return True
                    board[i][j]=word[0]
        
        return False

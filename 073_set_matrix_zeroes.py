"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def zero(i, j):
            for k in range(len(matrix)):
                if matrix[k][j]!=0:
                    matrix[k][j] = None
            for k in range(len(matrix[i])):
                if matrix[i][k]!=0:
                    matrix[i][k] = None
                        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero(i, j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

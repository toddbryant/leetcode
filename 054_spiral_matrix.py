"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def subspiral(matrix, i, j, m, n):
            if m<=0 or n<= 0:
                return []
            elif m>1 and n>1:
                result = matrix[i][j:j+n] 
                result += [matrix[c][j+n-1] for c in range(i+1, i+m)]
                result += [matrix[i+m-1][c] for c in range(i+n-2,i-1,-1)]
                result += [matrix[c][j] for c in range(i+m-2, i, -1)]
            elif m==1: # single row, multiple columns
                return matrix[i][j:j+n]
            elif n==1: # single column
                return [matrix[c][j] for c in range(i, i+m)]

    
            return result + subspiral(matrix, i+1, j+1, m-2, n-2)

        return subspiral(matrix, 0, 0, len(matrix), len(matrix[0]))

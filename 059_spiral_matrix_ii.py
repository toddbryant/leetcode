"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def fill(matrix, n, left, up, right, down):
            if left>right:
                return
            if left==right:
                matrix[left][up] = n
                return

            i, j = up, left
            while j<right:
                matrix[i][j] = n
                n += 1
                j += 1
            while i<down:
                matrix[i][j] = n
                n += 1
                i += 1
            while j>left:
                matrix[i][j] = n
                n += 1
                j -= 1
            while i>up:
                matrix[i][j] = n
                n += 1
                i -= 1
            fill(matrix, n, left+1, up+1, right-1, down-1)

        matrix = [ [0] * n for _ in range(n) ]
        fill(matrix, 1, 0, 0, n-1, n-1)
        return matrix 

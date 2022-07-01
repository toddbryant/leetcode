"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

# To rotate 90 degrees, row i becomes column n - i - 1
# column i becomes row i but reversed

# value at location (i,j) --> (j, n - i - 1)
# example 1:
# (0, 0) --> (0, 2)
# (0, 1) --> (1, 2)
# (0, 2) --> (2, 2)
# (1, 0) --> (0, 1)
# (1, 1) --> (1, 1)
# (1, 2) --> (2, 1)
# (2, 0) --> (0, 0)
# (2, 1) --> (1, 0)
# (2, 2) --> (2, 0)


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        not_fixed = set( ((i, j)) for i in range(0,n) for j in range(0,n))

        while not_fixed:
            i, j = not_fixed.pop()
            not_fixed.add((i,j))
            old_value = matrix[i][j]

            while True: # complete the cycle of fixes beginning at (i,j)
                i, j = j, n - i - 1
                if (i, j) not in not_fixed:
                    break
                tmp = matrix[i][j]
                matrix[i][j] = old_value
                not_fixed.remove((i, j)) 
                old_value = tmp


"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            element = matrix[mid//n][mid%n]
            if element == target:
                return True
            elif element < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False

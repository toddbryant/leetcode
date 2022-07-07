from functools import lru_cache
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache
        def count(i, j):
            if i==len(obstacleGrid) or j==len(obstacleGrid[0]) or obstacleGrid[i][j]==1:
                return 0
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                return 1
            return count(i+1, j) + count(i, j+1)
        
        return count(0, 0)

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

from typing import List

class Solution:
    """ Simply compute the max wall height to the left and right of each spot.
        Each spot will hold min(wall_left[i], wall_right[i]) - height[i] if that is positive.
    """
    def trap(self, height: List[int]) -> int:
        highest_wall_left = [0] * len(height)
        highest_wall_right = [0] * len(height)
        
        max_wall_left, max_wall_right = 0, 0
        for i in range(len(height)):
            highest_wall_left[i] = max_wall_left
            highest_wall_right[len(height) - i - 1] = max_wall_right
            max_wall_left = max(height[i], max_wall_left)
            max_wall_right = max(height[len(height) - i - 1], max_wall_right)
            
        trapped = 0
        for i in range(len(height)):
            wall_height = min(highest_wall_left[i], highest_wall_right[i])
            if wall_height > height[i]:
                trapped += wall_height - height[i]
        
        return trapped

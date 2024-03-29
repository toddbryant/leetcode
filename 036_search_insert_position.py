"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] < target:
                left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                return pivot

        return left
        

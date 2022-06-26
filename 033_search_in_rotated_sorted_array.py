"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while True:
            print('i,j = {}, {}'.format(i,j))
            m = (i + j) // 2
            if nums[i] < nums[m]:
                if nums[i] <= target <= nums[m]:
                    j = m
                else:
                    i = m
            elif nums[i] > nums[m]: # pivot in between
                if nums[m] <= target <= nums[j]:
                    i = m
                else:
                    j = m
            if nums[i]==target:
                return i
            if nums[j]==target:
                return j
            if i+1 >= j:
                break

        print('i,j = {}, {}'.format(i,j))
        return -1


                    

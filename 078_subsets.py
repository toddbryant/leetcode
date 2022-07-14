"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return([[nums[i] for i in range(len(nums)) if (x&(1<<i))] for x in range(1<<(len(nums)))])

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maintain dp[i] = length of maximum subarray ENDING at i
        # then dp[i+1] = max(dp[i+1], dp[i]+dp[i+1]) 
        # (basically use dp[i] if it is positive)
        # and since we don't need to reuse nums we can just use it
        # return max value of resulting array

        max_sub_array = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sub_array = max(max_sub_array, nums[i])

        return max_sub_array

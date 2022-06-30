"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""

from typing import List

class Solution:
    def jump_original(self, nums: List[int]) -> int:
        # Work backwards through the list
        # Maintain dp[i] = min jumps required to hit end of list
        # Then dp[i-1] = 1 + min(dp[i:i+nums[i-1]]), or 10000 if dp[i-1]=0
        
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i]==0:
                dp[i] = 10000
            else:
                dp[i] = 1 + min(dp[i+1:i+1+nums[i]])

        return dp[0]

    # new approach after reading solution
    def jump(self, nums: List[int]) -> int:
        farthest_index_reached = 0
        max_index_after_n_jumps = 0
        n_jumps = 0

        for i in range(len(nums) - 1):
            farthest_index_reached = max(farthest_index_reached, i + nums[i])
            
            if i == max_index_after_n_jumps:
                n_jumps += 1
                max_index_after_n_jumps = farthest_index_reached
        
        return n_jumps

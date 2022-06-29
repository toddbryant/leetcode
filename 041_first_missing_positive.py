"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Constraints:

1 <= nums.length <= 5 * 10^5
-231 <= nums[i] <= 231 - 1
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums:List[int]) -> int:
        # Cleaning up my solution based on super clean version I saw on leetcode
        length = len(nums)
        i = 0
        while i < length:
            correct_index = nums[i] - 1
            if 0 <= correct_index < length and nums[correct_index]!=nums[i]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i in range(length):
            if nums[i] != i+1:
                return i + 1

        return length + 1

    def firstMissingPositive_original(self, nums: List[int]) -> int:
        """ 
            Loop through list and 
            1) if num is nonpositive or above MAX_LEN, 0 it out
            2) swap each number into the i-1th index,
               so that a full set becomes [1,2,...,length]
            3) 0 out any duplicates (nums[n] already = n)
        """
        length = len(nums)
        for i in range(length):
            if nums[i]<1 or nums[i]>length:
                nums[i] = 0
            else:
                while nums[i]!=0 and nums[i]!=i+1:
                    # If out of range or destination already filled, kill this value
                    if nums[i]<1 or nums[i]>length or nums[nums[i] - 1] == nums[i]:
                        nums[i] = 0
                    else: # Otherwise, swap value into place
                        tmp = nums[nums[i] - 1]
                        nums[nums[i] - 1] = nums[i]
                        nums[i] = tmp

        for i, num in enumerate(nums):
            if num == 0:
                return i+1
    
        return length+1

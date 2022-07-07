"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i_first, j_first = 0, len(nums) - 1
        i_last, j_last = 0, len(nums) - 1 
        while i_first < j_first or i_last < j_last:
            print('i_first, j_first = {}, {}'.format(i_first, j_first))
            print('i_last, j_last = {}, {}'.format(i_last, j_last))
            m_first = (i_first + j_first) // 2
            m_last = (i_last + j_last) // 2

            if target == nums[m_first]:
                j_first = m_first
            elif target < nums[m_first]:
                j_first = m_first
            elif target > nums[m_first]:
                i_first = max(m_first, i_first + 1)

            if target == nums[m_last]:
                if i_last == m_last:
                    if nums[j_last] == target:
                        i_last = j_last
                    else:
                        j_last = i_last
                else:
                    i_last = m_last
            elif target < nums[m_last]:
                j_last = m_last
            elif target > nums[m_last]:
                i_last = max(m_last, i_last + 1)

        #print('i_first, j_first = {}, {}'.format(i_first, j_first))
        #print('i_last, j_last = {}, {}'.format(i_last, j_last))
        if i_first < len(nums) and nums[i_first] == target:
            return [i_first, i_last]

        return [-1, -1]
        

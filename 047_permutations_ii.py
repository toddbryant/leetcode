from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recurse(nums, start):
            if start == len(nums) - 1:
                result.append(nums[:]) # append copy of list 
            
            seen = set()
            for i in range(start, len(nums)):
                # swap ith element into beginning of this permutation
                if(nums[i] not in seen):
                    nums[i], nums[start] = nums[start], nums[i]
                    recurse(nums, start+1)
                    seen.add(nums[start])
                    nums[start], nums[i] = nums[i], nums[start] 
        
        recurse(nums, 0)
        return result


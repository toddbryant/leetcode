from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recurse(nums, start):
            if start == len(nums) - 1:
                result.append(nums[:]) # append copy of list 

            for i in range(start, len(nums)):
                # swap ith element into beginning of this permutation
                nums[i], nums[start] = nums[start], nums[i]
                recurse(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start] 
        
        recurse(nums, 0)
        return result


    # my original solution does the same but with more list copying
    def permute_original(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]

        result = []
        for i, n in enumerate(nums):
            for sublist in self.permute(nums[:i] + nums[i+1:]):
                result.append([n] + sublist)
        
        return result


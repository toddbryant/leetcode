/*
    Given an array nums of n integers and an integer target,
    find three integers in nums such that the sum is closest to target. 

    Return the sum of the three integers. 
    You may assume that each input would have exactly one solution.

    My solution modifies the improved algorithm from the previous problem.
    1) Sort the array.
    2) Iterate through all pivots--middle values of target sum.
    3) Work in from either side of the array:
        When the sum is too small, make the sum bigger by advancing from left.
        When the sum is too large, make the sum smaller by moving the right back.
   
    This solves the solution pretty quickly. 
*/

public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);            
        int closestSum = nums[0] + nums[1] + nums[2];
            
        for(int pivot=0; pivot<nums.Length; ++pivot) {
            int leftIndex = 0;
            int rightIndex = nums.Length - 1;

            while(leftIndex < pivot && rightIndex > pivot)
            {
                int currentSum = nums[pivot] + nums[leftIndex] + nums[rightIndex];
                
                if(Math.Abs(currentSum - target) < Math.Abs(closestSum - target)) {
                    closestSum = currentSum;
                }
                
                if(currentSum == target) { // We found the target, done
                    return target;
                }
                if(currentSum > target) { // Too big, make sum smaller
                    rightIndex--;
                }
                else if(currentSum < target) { // Too small, make sum bigger
                    leftIndex++;
                }
            }
        }
        
        return closestSum;
    }
}

/*
 * Given an array nums and a value val, remove all instances 
 * of that value in-place and return the new length.

 * Do not allocate extra space for another array, 
 * you must do this by modifying the input array in-place with O(1) extra memory.

 * The order of elements can be changed. 
 * It doesn't matter what you leave beyond the new length.
 */


/* Ugly but optimal: */

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int tail = nums.Length - 1;
        int i = 0;
        
        while(i <= tail) {
            if(nums[i] == val) { // Swap it to the end
                nums[i] = nums[tail];
                nums[tail] = val;
                --tail;
            }
            else {
                ++i;
            }
        }
        
        return tail + 1;
    }
}

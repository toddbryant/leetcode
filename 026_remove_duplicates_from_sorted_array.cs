public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int drop=0, seek=0;
        while(seek < nums.Length) {
            nums[drop] = nums[seek];
            while(seek < nums.Length && nums[drop] == nums[seek])
                ++seek;
            ++drop;
        }
    }
}

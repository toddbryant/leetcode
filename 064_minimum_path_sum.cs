/* 
 * Basic DP problem:
 *
 * Given a m x n grid filled with non-negative numbers, 
 * find a path from top left to bottom right 
 * which minimizes the sum of all numbers along its path.
 *
 * We use DP with a cache.
 */

public class Solution {
    Dictionary<int, int> memo = new Dictionary<int, int>();
    
    public int MinPathToTop(int[][] grid, int i, int j) {
        if(i==0 && j==0) // Base case
            return grid[i][j];
        int pos = i + j * grid.Length; // serialize coordinates
        
        // Only do work if this position isn't cached
        int ret; // We shave a couple ms by avoiding a second lookup
        if(!memo.TryGetValue(pos, out ret)) {
            if(j==0) // Can only go up
                ret = grid[i][j] + MinPathToTop(grid, i-1, j);
            else if (i==0) // Can only go left
                ret = grid[i][j] + MinPathToTop(grid, i, j-1);
            else
                ret = grid[i][j] + Math.Min(MinPathToTop(grid, i-1, j), MinPathToTop(grid, i, j-1));
           memo[pos] = ret;
        }
            
        return ret;
    }
    
    public int MinPathSum(int[][] grid) {
        return MinPathToTop(grid, grid.Length - 1, grid[0].Length - 1);
    }
}

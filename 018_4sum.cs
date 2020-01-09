/*
    This solution is ugly as sin but gets the job done

    Okay so the optimal solution here was to sort the list,
    then recursively look for N-1 sums, until we reduce to 2sum. 
    Then we use the converging pointer algorithm.
*/

public class IntListEqualityComparer : IEqualityComparer<IList<int>> {
    public bool Equals(IList<int> t1, IList<int> t2) {
        // lazily assume lengths of 4 for both lists
        for(int i=0; i<4; ++i)
            if(t1[i] != t2[i])
                return false;
        
        return true;
    }
    
    public int GetHashCode(IList<int> list)
    {
        int result = 0;
        foreach(int i in list) {
            result ^= i;
        }
        return result.GetHashCode();
    }
        
}

public class Solution {
    public IList<IList<int>> FourSum(int[] nums, int target) {
        // Compute counts for each element in the list
        Dictionary<int, int> counts = new Dictionary<int, int>();
        foreach(int num in nums) {
            if(!counts.ContainsKey(num)) {
                counts[num] = 0;
            }
            ++counts[num];
        }
        
        Dictionary<int, List<Tuple<int, int>>> pairSums = new Dictionary<int, List<Tuple<int, int>>>();
        HashSet<IList<int>> solutions = new HashSet<IList<int>>(new IntListEqualityComparer());
        
        // Compute all unique sums in the list
        for(int i=0; i<nums.Length; ++i) {
            for(int j=i+1; j<nums.Length; ++j) {
                int sum = nums[i] + nums[j];
                if(!pairSums.ContainsKey(sum)) {
                    pairSums[sum] = new List<Tuple<int, int>>();
                }
                pairSums[sum].Add(new Tuple<int, int>(nums[i],nums[j]));    
            }
        }
        
        int[] solution = new int[4];
        foreach(int sum in pairSums.Keys){
            if(pairSums.ContainsKey(target-sum)) {
                foreach(Tuple<int, int> tuple in pairSums[sum]) {
                    foreach(Tuple<int, int> other_tuple in pairSums[target-sum]) {
                        solution[0] = tuple.Item1;
                        solution[1] = tuple.Item2;
                        solution[2] = other_tuple.Item1;
                        solution[3] = other_tuple.Item2;
                 
                        // Check that this solution doesn't overuse any elements
                        Dictionary<int, int> solutionCounts = new Dictionary<int, int>();
                        foreach(int num in solution) {
                            if(!solutionCounts.ContainsKey(num)) {
                                solutionCounts[num] = 0;
                            }
                            solutionCounts[num]++;
                        }
                        
                        int i;
                        for(i=0; i<4; ++i) 
                        {
                            if(solutionCounts[solution[i]] > counts[solution[i]]) // invalid solution
                                break;
                        }
                        
                        if(i==4) { // solution was validated
                            Array.Sort(solution);
                            solutions.Add(new List<int>(solution));
                        }
                    }
                }
            }
        }
        
        return solutions.ToList();
    }
}

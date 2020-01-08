/*
    Given an array nums of n integers, are there elements 
    a, b, c in nums such that a + b + c = 0? 
    
    Find all unique triplets in the array which gives the sum of zero.

    My first solution is based on considering all pairs of (n, p) in nums
    such that n is negative and p is positive (required for all triples except (0,0,0)).

    We then simply search for -(n+p) in the original list, with handling for duplicates. 

    This is a first draft that can be simplified.
*/



public class TripleEqualityComparer : IEqualityComparer<IList<int>> {
    public bool Equals(IList<int> t1, IList<int> t2) {
        List<int> triple1 = (List<int>)t1;
        List<int> triple2 = (List<int>)t2;
        triple1.Sort();
        triple2.Sort(); 
        return (triple1[0] == triple2[0] && triple1[1] == triple2[1] && triple1[2] == triple2[2]);
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
    public IList<IList<int>> ThreeSum(int[] nums) {
        TripleEqualityComparer comp = new TripleEqualityComparer();
        HashSet<IList<int>> solutions = new HashSet<IList<int>>(comp);
        
        Dictionary<int, int> values_with_counts = new Dictionary<int, int>();
        foreach(int num in nums)
        {
            if(values_with_counts.ContainsKey(num)) {
                values_with_counts[num]++;
            } 
            else {
                values_with_counts[num] = 1;
            }
        }
        
        List<int> positives = nums.Where(i => i>=0).ToList();
        List<int> negatives = nums.Where(i => i<0).ToList();
        
        foreach(int pos in positives) {
            foreach(int neg in negatives) {
                int target = -(pos+neg);
                if(values_with_counts.ContainsKey(target)) {
                    List<int> solution = new List<int> {neg, target, pos};
                    solution.Sort();
                    if(target == neg || target == pos) { // target equal to neg or pos
                        if(values_with_counts[target] > 1)
                            solutions.Add(solution);
                    }
                    else {
                        solutions.Add(solution);
                    }
                }
            }
        }
        
        if(values_with_counts.ContainsKey(0) && values_with_counts[0] >= 3) {
            solutions.Add(new List<int> {0, 0, 0});
        }
        
        List<IList<int>> ret = solutions.ToList();
        return solutions.ToList();
        
    }
}

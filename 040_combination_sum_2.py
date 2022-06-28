"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        counts = {}
        for i in candidates:
            if i not in counts:
               counts[i] = 0
            counts[i] += 1
        candidates = sorted(counts.keys())
        
        def backtrack(target, combination, start):
            if target==0:
                results.append(list(combination))
                return
            if target<0 or start>=len(candidates):
                return
            
            for i in range(start, len(candidates)):
                for c in range(counts[candidates[i]], 0, -1):
                   backtrack(target-candidates[i]*c, combination+[candidates[i]]*c, i+1)
                
        backtrack(target, [], 0)
        
        return results

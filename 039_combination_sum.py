"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

from typing import List

class Solution:
    """
        dp[n] = [[dp[n-c],c] for c in candidates]
        dp[0] = [[]]
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recurse(candidates, target, {})

    def recurse(self, candidates, target, memo):
        if target == 0:
            return [[]]
        if target < 0:
            return []

        if target not in memo:
            memo[target] = set()
            for n in candidates:
                for partialSum in self.recurse(candidates, target - n, memo):
                    memo[target].add(tuple(sorted(list(partialSum)+[n])))

        return [list(x) for x in memo[target]]

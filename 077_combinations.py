"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = [0 for _ in range(k)]
        
        def backtrack(start, i):
            if i==k:
                result.append(list(current))
            else:
                for j in range(start, n-k+i+2):
                    current[i] = j
                    backtrack(j+1, i+1)
                    
        backtrack(1,0)
        return result

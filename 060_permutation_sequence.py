"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k=k-1 # make k 0-based
        result = []
        digits = list(range(1,n+1))
        total = math.factorial(n)
        while n:
            i, k = k // (total//n), k % (total//n)
            total, n = total//n, n-1
            result.append(str(digits.pop(i)))
        return ''.join(result)

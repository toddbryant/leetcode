"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def lev(i, j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return lev(i+1, j+1)
            return 1 + min(lev(i+1, j), lev(i, j+1), lev(i+1, j+1))

        return lev(0,0)

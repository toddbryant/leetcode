"""
  Given two strings needle and haystack, return the index of the first occurrence 
  of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Trickier solution with some quick short circuiting
        try:
            for i in range(len(haystack)):
                if haystack[i]==needle[0] and haystack[i+len(needle)-1]==needle[-1] and haystack[i:].startswith(needle):
                    return i
        except:
            raise
            pass
        return -1

    """ Naive solution about as good as short circuiting one """
    def simple_strStr(self, haystack: str, needle: str) -> int:
        # Naive solution
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

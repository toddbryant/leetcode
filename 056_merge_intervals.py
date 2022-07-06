"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Returns True if two intervals overlap
        def overlap(interval1, interval2):
            s1, e1 = interval1
            s2, e2 = interval2
            return not (s1 > e2 or s2 > e1)

        subtrees = []
        for interval in intervals:
            i = 0
            while i < len(subtrees):
                tree = subtrees[i]
                if interval[1] < tree[0]:
                    i += 1
                elif overlap(interval, tree):
                    interval = [min(interval[0], tree[0]),max(interval[1], tree[1])]
                    subtrees.pop(i)
                elif interval[0] > tree[1]:
                    break
            subtrees.insert(i, interval)
        
        return subtrees


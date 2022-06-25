"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        # dict of start index --> stop index
        # of substrings of well formed parentheses
        well_formed_parens = {}

        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                try:
                    start_index = stack.pop()
                    well_formed_parens[start_index] = i
                except IndexError:
                    pass
                
        current_start, current_end = -2, -2
        max_start, max_end = 0, -1

        # Merge adjacent groups together
        for i in sorted(well_formed_parens.keys()):
            if well_formed_parens[i] > current_end:
                if i!=current_end + 1:
                    current_start = i
                current_end = well_formed_parens[i]
                if current_end - current_start > max_end - max_start:
                    max_start, max_end = current_start, current_end

        return max_end - max_start + 1

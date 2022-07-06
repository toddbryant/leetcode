"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        result = []
        while i<len(words):
            # Pull out as many words as possible
            line = []
            line_length = 0
            while i < len(words) and ((line_length + len(line) + len(words[i])) <= maxWidth):
                line.append(words[i])
                line_length += len(words[i])
                i += 1
                
            # Divide spaces across the line
            if i<len(words):
                total_spaces = maxWidth - line_length
                
                result.append([])
                if len(line) > 1:
                    space_width, carry = divmod(total_spaces, len(line)-1)
                    for j, word in enumerate(line):
                        result[-1].append(word)
                        if j < len(line)-1:
                            result[-1].append(' '*(space_width + (1 if j < carry else 0)))
                    #print('before join join result[-1] is {}'.format(result[-1]))
                    result[-1] = ''.join(result[-1])
                else:
                    result[-1] = line[0] + (' ' * (maxWidth-len(line[0])))
            else:
                result.append(' '.join(line))
                result[-1] = result[-1] + (' ' * (maxWidth-len(result[-1])))
            
        
        return result

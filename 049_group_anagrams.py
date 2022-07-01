"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy:
        # sort each word for its key
        # map sorted word --> list of original words

        words_by_key = {}
        def make_key(word):
            counts = [0] * 26        
            for c in word:
                counts[ord(c) - ord('a')] += 1
            return tuple(counts)

        for word in strs:
            key = make_key(word)
            # key = ''.join(sorted(word))
            if key not in words_by_key:
                words_by_key[key] = []                
            words_by_key[key].append(word)

        return [word_list for _, word_list in words_by_key.items()]

"""
   You are given a string s and an array of strings words of the same length. 
   Return all starting indices of substring(s) in s that is a concatenation 
   of each word in words exactly once, in any order, and without any intervening characters.

   You can return the answer in any order.
"""

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.target_word_counts = {}
        for word in words:
            if word not in self.target_word_counts:
                self.target_word_counts[word] = 0
            self.target_word_counts[word] += 1
        print('target word counts is {}'.format(self.target_word_counts)) 

        letter_counts = {}
        substring_length = len(words[0]) * len(words)

        target_letter_counts = {}
        for word in words:
            for c in word:
                if c not in target_letter_counts:
                    target_letter_counts[c] = 0
                target_letter_counts[c] += 1

        print('target letter counts is {}'.format(target_letter_counts))


        indexes = []
        for i, c in enumerate(s):
            print('=========== {}: {} ======='.format(i, c))
            if c not in letter_counts:
                letter_counts[c] = 0

            letter_counts[c] += 1
            if i >= substring_length: # Remove old character
                print('Removing {} from letter_counts'.format(s[i-substring_length]))
                letter_counts[s[i-substring_length]] -= 1
                if letter_counts[s[i-substring_length]] == 0:
                    del letter_counts[s[i-substring_length]]
            print('letter_counts is now {}'.format(letter_counts))
            
            if letter_counts == target_letter_counts:
                if self.checkForSubstringAt(s, words, i - substring_length + 1):
                    indexes.append(i - substring_length + 1)

        return indexes

    # Returns True if s[i] is the start of a substring
    def checkForSubstringAt(self, s: str, words:List[str], i: int) -> bool:
        print('Checking for substring at {}'.format(i))
        word_counts = {}
        word_length = len(words[0])
        for j in range(i, i + len(words) * word_length, word_length):
            word = s[j:j+word_length]
            print('word: {}'.format(word))
            if word not in self.target_word_counts:
                return False
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
        print('observed word counts is {}'.format(word_counts)) 
            
        return self.target_word_counts == word_counts

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = Counter(t)
        current_counts = Counter()
        left, right = 0, -1
        window_made = False
        best_window = ""
        
        while left < len(s):
            #print(f'{s[left:right+1]}')
            #print(f'{current_counts}')
            if window_made:
                if s[left] in target_counts and current_counts[s[left]] == target_counts[s[left]]:
                    window_made = False
                current_counts[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right==len(s):
                    break
                if s[right] in target_counts:
                    current_counts[s[right]] += 1
                if all(current_counts[c] >= target_counts[c] for c in target_counts):
                    window_made = True
            if window_made and (best_window=="" or len(best_window) > (right - left + 1)):
                best_window = s[left:right+1]
        
        return best_window

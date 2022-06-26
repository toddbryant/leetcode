"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for i in range(n-1):
            count_and_say = []
            current_digit, current_digit_count = s[0], 1
            for digit in s[1:]:
                if digit != current_digit:
                    count_and_say.append(str(current_digit_count) + str(current_digit))
                    current_digit = digit
                    current_digit_count = 1
                else:
                    current_digit_count += 1

            count_and_say.append(str(current_digit_count) + str(current_digit))
            
            s = ''.join(count_and_say)            

        return s

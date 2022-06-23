"""
    Given two integers dividend and divisor, divide two integers 
    without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, 
    which means losing its fractional part. 
    For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers 
    within the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
    
    For this problem, if the quotient is strictly greater than 231 - 1, 
    then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

from math import exp, log

class Solution:
    MAX_POSITIVE_ANSWER = (2<<30) - 1
    MAX_NEGATIVE_ANSWER = (2<<30)
    EPSILON = 0.00000000001 # hack for roundoff

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        answer_is_negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        answer = int(exp(log(abs(dividend)) - log(abs(divisor))) + EPSILON)
        
        if answer_is_negative:
            return -min(self.MAX_NEGATIVE_ANSWER, answer)
        else:
            return min(self.MAX_POSITIVE_ANSWER, answer)


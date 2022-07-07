"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x

        hi, lo, guess = x, 0, x//2
        while hi>guess>lo:
            if guess * guess == x:
                return guess
            elif guess * guess < x:
                lo, guess, hi = guess, (hi + guess)//2, hi
            elif guess * guess > x:
                lo, guess, hi = lo, (lo + guess)//2, guess
        return guess
    

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        d1_power_ten = 1
        for digit in num1[::-1]:
            d2_power_ten = 1
            for digit2 in num2[::-1]:
                product += d1_power_ten * d2_power_ten * (ord(digit2)-48) * (ord(digit)-48)
                d2_power_ten *= 10
            d1_power_ten *= 10
        return str(product)
        

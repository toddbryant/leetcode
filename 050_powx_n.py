"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x = 2^log2(x)

        if x==0:
            return 0
        if n==0:
            return 1

        was_negative = n < 1
        n = abs(n)
        # convert n to binary
        # for each 1 in binary representation of n, square x that many times
        # ex: n = 19 --> 10011
        # x^n = x * x^2 * x^16
        binary_n = bin(n)[2:]
    
        result = 1.0
        for pwr, bit in enumerate(binary_n[::-1]):
            if bit=="1":
                piece = x
                for i in range(0, pwr):
                    piece = piece * piece
                result *= piece
        
        if was_negative:
            return 1.0/result
        return result                       

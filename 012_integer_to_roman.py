import unittest 

SYMBOLS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), \
           (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), \
           (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

class TestIsMatch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(integerToRoman(3), "III")

    def test_2(self):
        self.assertEqual(integerToRoman(4), "IV")

    def test_3(self):
        self.assertEqual(integerToRoman(9), "IX")

    def test_4(self):
        self.assertEqual(integerToRoman(58), "LVIII")

    def test_5(self):
        self.assertEqual(integerToRoman(1994), "MCMXCIV")

def integerToRoman(n):
    result = ""
    i = 0
    while n:
       while SYMBOLS[i][0] > n:
           i += 1 
       val, sym = SYMBOLS[i]
       result += sym * (n//val)
       n -= val * (n//val)
    return result

if __name__=='__main__':
    unittest.main()

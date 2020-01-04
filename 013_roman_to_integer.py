import unittest 

SYMBOLS = {"M":1000, "CM":900, "D":500, "CD":400, \
           "C":100, "XC":90, "L":50, "XL":40, \
           "X":10, "IX":9, "V":5, "IV":4, "I":1}

class TestIsMatch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(romanToInteger("III"), 3)

    def test_2(self):
        self.assertEqual(romanToInteger("IV"), 4)

    def test_3(self):
        self.assertEqual(romanToInteger("IX"), 9)

    def test_4(self):
        self.assertEqual(romanToInteger("LVIII"), 58)

    def test_5(self):
        self.assertEqual(romanToInteger("MCMXCIV"), 1994)

def romanToInteger(roman):
    result, i = 0, 0
    while i < len(roman):
       try: 
           result += SYMBOLS[roman[i:i+2]] 
           i += 2 
       except:
           result += SYMBOLS[roman[i]]
           i += 1
    
    return result

if __name__=='__main__':
    unittest.main()

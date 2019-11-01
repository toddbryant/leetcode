import unittest 

class TestIsMatch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isMatch("aa", "a"), False)

    def test_2(self):
        self.assertEqual(isMatch("aa", "a*"), True)

    def test_3(self):
        self.assertEqual(isMatch("ab", ".*"), True)

    def test_4(self):
        self.assertEqual(isMatch("aab", "c*a*b"), True)

    def test_5(self):
        self.assertEqual(isMatch("mississippi", "mis*is*p*."), False)

    def test_tricky_1(self):
        self.assertEqual(isMatch("six", ".*x"), True)

    def test_tricky_2(self):
        self.assertEqual(isMatch("app", "ap*p"), True)

    def test_tricky_3(self):
        self.assertEqual(isMatch("mississippi", "mis*is*ip*."), True)

def isMatch(s, p):
    cache = {}
    def dpIsMatch(s_index, p_index):
        if (s_index, p_index) not in cache:
            if p_index == len(p): # Empty pattern requires empty string
                result = s_index == len(s)
            else:
                if p_index + 1 < len(p) and p[p_index+1] == "*": # Klein star
                    if s_index < len(s) and (p[p_index] == s[s_index] or p[p_index] == "."):
                        # Found element. We can consume it, or not.
                        result = dpIsMatch(s_index+1, p_index) or dpIsMatch(s_index, p_index+2)
                    else: # First character doesn't match pattern. Match 0 and continue.
                        result = dpIsMatch(s_index, p_index+2)
                else: # No Klein star. Match a single element.
                    if s_index == len(s) or (s[s_index] != p[p_index] and p[p_index] != "."):
                        # Failed to match a required character
                        result = False
                    else: 
                        # Matched required character. Consume it and continue.
                        result = dpIsMatch(s_index+1, p_index+1)
            cache[(s_index, p_index)] = result

        return cache[(s_index, p_index)]

    return dpIsMatch(0, 0)

if __name__=='__main__':
    unittest.main()

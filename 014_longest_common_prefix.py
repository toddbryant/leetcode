import unittest 

class TestIsMatch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_2(self):
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")

# Returns the longest common prefix of two strings
def lcp_pair(a, b):
    i = 0
    while i < len(a) and i < len(b):
        if a[i] != b[i]:
            return a[:i]
        i += 1

    return a if len(a) < len(b) else b

def longestCommonPrefix(strs):
    if(len(strs)) == 0:
        return ""
    if(len(strs)) == 1:
        return strs[0]

    lcp = strs[0]
    for s in strs[1:]:
        lcp = lcp_pair(s, lcp)

    return lcp

if __name__=='__main__':
    unittest.main()

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print('isMatch {}, {}'.format(s,p))
        while '**' in p:
            p = p.replace('**', '*')
        if not s:
            return all(c=='*' for c in p)
        elif not p: # more string but no pattern
            return False
        elif p[0]=='?':
            return self.isMatch(s[1:], p[1:])
        elif p[0]=='*':
            if len(p)==1:
                return True
            elif p[1]=='?':
                return self.isMatch(s[1:], p[1:])
            else:
                
            return any((self.isMatch(s[i:], p[1:]) for i in range(0, len(s)+1)))
        else:
            return s[0]==p[0] and self.isMatch(s[1:], p[1:])

"babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

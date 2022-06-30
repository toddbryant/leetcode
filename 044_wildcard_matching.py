class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while '**' in p:
            p=p.replace('**', '*')
        memo = {}
        
        def isMatchRecursive(s, p):
            if (s, p) not in memo:
                if not s:
                    result = all(c=='*' for c in p)
                elif not p: # more string but no pattern
                    result = False
                elif p[0]=='?':
                    result = isMatchRecursive(s[1:], p[1:])
                elif p[0]=='*':
                    result = isMatchRecursive(s, p[1:]) or isMatchRecursive(s[1:], p)
                else:
                    result = s[0]==p[0] and isMatchRecursive(s[1:], p[1:])
                memo[(s,p)] = result
            
            return memo[(s,p)]

        
        return isMatchRecursive(s, p)
    
    
        

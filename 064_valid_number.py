class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        if s[i] in ['+', '-']:
            i += 1
        dot_seen, e_seen, digit_seen = False, False, False
        while i < len(s):
            if s[i]=='.':
                if dot_seen:
                    return False
                dot_seen = True
            elif s[i] in ['e', 'E']:
                if e_seen or not digit_seen:
                    return False
                e_seen = True
                digit_seen = False
                dot_seen = True
                if i+1 < len(s) and s[i+1] in ['+', '-']:
                    i += 1
            elif ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return False
            else:
                digit_seen = True
            
            i += 1
        
        return digit_seen

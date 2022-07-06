class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

    # original solution assuming I can't use bin
    def addBinary_original(self, a: str, b: str) -> str:
        if a=='0' and b=='0':
            return '0'
        result = ['0'] * (max(len(a), len(b)) + 1)
        i = 0
        carry = 0
        while i<len(a) or i<len(b):
            d1 = a[-1-i] if i<len(a) else "0"
            d2 = b[-1-i] if i<len(b) else "0"
            if d1=="0" and d2=="0":
                result[-1-i]="1" if carry else "0"
                carry = 0
            elif d1=="1" and d2=="1":
                result[-1-i] = "1" if carry else "0"
                carry = 1
            else:
                if carry:
                    result[-1-i] = "0"
                    carry = 1
                else:
                    result[-1-i] = "1"
                    carry = 0
            
            i += 1
        
        if carry:
            result[-1-i]="1"
        result = ''.join(result)
        return result[result.index("1"):]

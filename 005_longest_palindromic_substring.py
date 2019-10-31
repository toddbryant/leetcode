### leetcode 005: 
### Find the longest palindromic substring in a string
###
### We search for palindromes at each index,
### starting from th middle and working out.
### Odd and even length palindromes are handled separately.

def longestPalindrome(s):
    if not s:
        return ""
    max_length = 1
    max_palindrome = s[0]
    for start in range(len(s)):
        # Find odd palindromes
        l, r, length = start-1, start+1, 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length += 2
            l -= 1
            r += 1
        if length > max_length:
            max_length = length
            max_palindrome = s[l+1:r]

        # Find even palindromes
        l, r, length = start, start+1, 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length += 2
            l -= 1
            r += 1
        if length > max_length:
            max_length = length
            max_palindrome = s[l+1:r]

    return max_palindrome

if __name__ == "__main__":
    # Didn't test much as algorithm is very straightforward
    print(longestPalindrome("suprcalifragilisticxyxyxyxyxyxypneumonoultramicroscopicsilicovolcanoconiosis"))

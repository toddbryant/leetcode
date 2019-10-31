# This is a trivial problem that tests whether an int is a palindrome
# However the trick is that the solution below is super fast in Python.

def isPalindrome(self, x: int) -> bool:
    return str[x]==str[x::-1]

import string 

def atoi(s):
    i = 0
    result = 0
    sign = 1
    try:
        # Consume all whitespace
        while s[i]==" ":
            i += 1
        # Handle optional minus sign
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+"
            i += 1
        # Consume all consecutive digits
        while s[i] in string.digits:
            result = result * 10 + int(s[i])
            i += 1
    except IndexError:
        pass
    result *= sign

    # Handle overflow
    if result >= 2**31:
        result = 2**31 - 1
    elif result < -2**31:
        result = -2**31

    return result

def test():
    cases = [
             ("", 0), \
             ("    ", 0), \
             ("    42", 42), \
             ("    -42", -42), \
             ("    -123442", -123442), \
             ("    -123442 words at end", -123442), \
             ("    -123442 words at end", -123442), \
            ]
    for case in cases:
        try:
            assert atoi(case[0]) == case[1]
        except AssertionError:
            print("ERROR:")
            print("Input: {0}".format(case[0]))
            print("Expected: {0}".format(case[1]))
            print("Got: {0}".format(atoi(case[0])))


if __name__ == '__main__':
    test()

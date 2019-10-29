def fractionToDecimal(numerator: int, denominator: int) -> str:
    # Deal with negative signs first
    sign = "-" if numerator*denominator < 0 else ""
    numerator, denominator = abs(numerator), abs(denominator)

    # Reduce to numerator < denominator
    integer_part = str(numerator//denominator)
    numerator = numerator % denominator

    fractions_seen = {(numerator, denominator): 0}
    numerator *= 10 
    decimal_part = ""
    place = 1

    while numerator:
        # Record the new fraction or break if loop has been reached
        if (numerator, denominator) in fractions_seen:
            first_seen = fractions_seen[(numerator, denominator)] - 1
            decimal_part = decimal_part[0:first_seen] + "(" + decimal_part[first_seen:] + ")"
            break
        else:
            fractions_seen[(numerator, denominator)] = place

        # Advance long division
        if numerator < denominator:
            decimal_part += "0"
            numerator *= 10
        else:
            decimal_part += str(numerator//denominator)
            numerator = 10 * (numerator % denominator)

        place += 1 

    # Only add a decimal point if there was a decimal part
    if decimal_part:
            decimal_part = "." + decimal_part

    return sign + integer_part + decimal_part

def test():
    test_cases = {}
    test_cases[(-12, 1)] = "-12"
    test_cases[(4, 2)] = "2"
    test_cases[(2, 3)] = "0.(6)"
    test_cases[(1, 7)] = "0.(142857)"
    test_cases[(7, 12)] = "0.58(3)"
    test_cases[(9, 11)] = "0.(81)"
    test_cases[(22, 7)] = "3.(142857)"
    test_cases[(-12, -999)] = "0.(012)"

    for (case, expected) in test_cases.items():
        got = fractionToDecimal(*case)
        try:
            assert got == expected
        except:
            print("ERROR:")
            print("Expected: {0} --> {1}".format(case, expected))
            print("Got: {0} --> {1}".format(case, got))

if __name__ == "__main__":
    test()

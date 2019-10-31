# The string "PAYPALISHIRING" is written 
# in a zigzag pattern on a given number of rows like this:
# P   A   H   N    <-- row 0 (length s)/n
# A P L S I I G    <-- row 1 (length s)/n * 2 - 1
# Y   I   R        <-- row 2 (length s)/n - (length s)%n
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

def convert(s, n):
    # Zigzagify a string
    row = 0
    direction = 1 if n > 1 else 0
    grid = [[] for i in range(n)]
    for c in s:
        grid[row].append(c)
        row += direction
        if row == n-1 or row == 0:
            direction *= -1 # Turn around
    return ''.join([''.join(r) for r in grid])

if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3))

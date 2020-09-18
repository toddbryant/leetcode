# Given an array S of ints, find the next permutation that orders after S
# Examples:
# [1,2,3] --> [1,3,2]
# [2,5,7,3,4,1] --> [2,5,7,4,1,3]
# [3,2,1] --> [1,2,3]

# Facts:
# For a decreasing sequence D = d0, d1, ..., dn
# the next permutations is dn, dn-1, ..., d0

# For a sequence a0 plus a decreasing sequence D = d0, d1, ..., dn
# with a0 < d0, we find the next sequence as follows:
# 1) Reverse D, making D' = dn, dn-1, ..., d0
# 2) Swap a0 with the first element of D' that is greater than a0
# This gives di, dn, dn-1, ..., a0, di-1, di-2, ..., d0
# Since di > a0, the sequence orders after a0, d0, d1, ..., dn
# The remaining elements are now in ascending order, so no sequence orders before them.

def next_perm(arr):
    # Find the largest decreasing sequence from the end of the array
    i = len(arr) - 2
    while i>=0:
        if(arr[i] < arr[i+1]):
            break
        i = i -1
    if i<0: # The whole array was decreasing
        return arr[::-1]

    # 1) Reverse the decreasing sequence
    arr[i+1:] = arr[i+1:][::-1] 
    # 2) Swap a0 with the first elemnt of D' greater than a0
    j = i + 1
    while arr[j] <= arr[i]:
        j += 1
    arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == '__main__':
    # lazy
    assert next_perm([1,2,3]) == [1,3,2]
    assert next_perm([2,5,7,3,4,1]) == [2,5,7,4,1,3]
    assert next_perm([3,2,1]) == [1,2,3]

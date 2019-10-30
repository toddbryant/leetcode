import sys

def kthElement(A, a_start, B, b_start, k):
    # Finds the kth element of two sorted arrays.
    if k >= len(A) + len(B):
        raise ValueError("Requested index exceeds total array lengths.")

    # Deal with 0 length arrays
    if a_start >= len(A):
        return B[b_start + k]
    if b_start >= len(B):
        return A[a_start + k]

    # Base case
    if k==0:
        return min(A[a_start], B[b_start])

    # Check index k//2 in both arrays
    try:
        elem_A = A[a_start + (k+1)//2 - 1 ]
    except IndexError:
        elem_A = sys.maxsize

    try:
        elem_B = B[b_start + (k+1)//2 - 1]
    except IndexError:
        elem_B = sys.maxsize

    # Remove the smaller set of (k+1)//2 elements
    if elem_A < elem_B:
        return kthElement(A, a_start + (k+1)//2, B, b_start, k - (k+1)//2)
    else:
        return kthElement(A, a_start, B, b_start + (k+1)//2, k - (k+1)//2)

def findMedianSortedArrays(nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 0:
            return ((kthElement(nums1, 0, nums2, 0, (m + n)//2 - 1)) + \
                    (kthElement(nums1, 0, nums2, 0, (m + n)//2))) / 2.0
        else:
            return kthElement(nums1, 0, nums2, 0, (m + n)//2)

def test():
    cases = [ \
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], \
            [[1, 6], [2, 3, 5, 6]], \
            [[3, 5, 99, 100, 101], [0, 1, 2, 99999]] \
            ]

    for pairs in cases:
        A, B = pairs[0], pairs[1]
        combined = sorted(A + B)
        for n in range(len(A) + len(B)):
            try:
                assert kthElement(A, 0, B, 0, n) == combined[n]
            except:
                print("A={0}".format(A))
                print("B={0}".format(B))
                print("combined={0}".format(combined))
                print("n={0}".format(n))
                print("Expected: {0}\nGot: {1}".format(combined[n], kthElement(A, 0, B, 0, n)))
                raise AssertionError
    
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert findMedianSortedArrays([1, 3], [2]) == 2.0

def main():
    test()

if __name__ == '__main__':
    main()

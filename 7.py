A=input("write?")
def longestPalindrome(A):
    rev = A[::-1]
    l = len(A)
    while l > 0:
        for i in range(0, len(A) - l + 1):
            half = int(l / 2)
            left = A[i : i + half]
            right = rev[len(A) - (i + l) : len(A) - (i + l - half)]
            if left == right:
                return A[i:i+l]
        l -= 1
    return None
print (longestPalindrome(A))

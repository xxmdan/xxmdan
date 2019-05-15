def check_palindrome(s):
    return s == s[::-1]

max_product = 0
a = b = 0

for i in range(999, 900, -1):
    for j in range(i, 900, -1):
        product = i * j
        if check_palindrome(str(product)):
            if product > max_product:
                max_product = product
                a = i
                b = j
print(a, "*", b, "=", max_product)

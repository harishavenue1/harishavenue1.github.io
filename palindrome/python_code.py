def is_palindrome(s):
    return s == s[::-1]

str = "radar"
if is_palindrome(str):
    print(str + " is a palindrome.")
else:
    print(str + " is not a palindrome.")

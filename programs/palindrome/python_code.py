def is_palindrome(s):
    
    # Python: String slicing [::-1] reverses the string
    # Compare original with reversed using == operator
    return s == s[::-1]

str = "radar"
if is_palindrome(str):
    print(str + " is a palindrome.")
else:
    print(str + " is not a palindrome.")

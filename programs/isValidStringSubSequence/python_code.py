def isValidSubSequence(s1, s2):
    
    # Python: Get string lengths using len() function
    m = len(s1)
    n = len(s2)

    
    # Python: Pointer for subsequence string
    j = 0
    
    # Python: Iterate through main string using range()
    for i in range(n):
        
        # Python: Direct character comparison using indexing
        if s1[j] == s2[i]:
            j = j + 1  # Move subsequence pointer forward
    
    
    # Python: Check if all characters of subsequence were found
    return j == m

str1 = 'gksr%ek@@@'
str2 = 'geeksforge%eks@@@'
isValid = isValidSubSequence(str1, str2)
print('Valid SubSequence', isValid)
def isValidSubSequence(s1, s2):
    m = len(s1)
    n = len(s2)

    j = 0
    for i in range(n):
        if s1[j] == s2[i]:
            j=j+1
    
    return j==m

str1 = 'gksr%ek@@@'
str2 = 'geeksforge%eks@@@'
isValid = isValidSubSequence(str1, str2)
print('Valid SubSequence', isValid)
def missingNum(nums):
    
    # Python: Get array length using len()
    arrLen = len(nums)
    
    # Python: Calculate expected sum using arithmetic series formula
    expectedSum = int(((arrLen * (arrLen+1))/2))
    
    # Python: Built-in sum() function for actual sum
    actualSum = sum(nums)
    
    
    # Python: Missing number is difference between expected and actual
    return expectedSum - actualSum

arr = [3,0,1]
miss_num = missingNum(arr)
print('Missing Number is', miss_num)

arr = [0,1]
miss_num = missingNum(arr)
print('Missing Number is', miss_num)

arr = [9,6,4,2,3,5,7,0,1]
miss_num = missingNum(arr)
print('Missing Number is', miss_num)
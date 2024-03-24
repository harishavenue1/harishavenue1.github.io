def missingNum(nums):
    arrLen = len(nums)
    expectedSum = int(((arrLen * (arrLen+1))/2))
    actualSum = sum(nums)
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
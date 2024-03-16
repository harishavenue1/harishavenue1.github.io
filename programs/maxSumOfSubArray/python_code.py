def maxSumOfSubArray(nums):
    arrLen = len(nums)
    currSum = nums[0]
    maxSum = nums[0]

    for i in range(1, arrLen):
        currSum = currSum + nums[i]
        if currSum < 0:
            currSum = 0
        maxSum = max(maxSum, currSum)

    return maxSum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))

arr = [1]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))

arr = [5,4,-1,7,8]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))
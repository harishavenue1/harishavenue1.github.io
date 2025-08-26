def maxSumOfSubArray(nums):
    
    # Python: Kadane's Algorithm for maximum subarray sum
    arrLen = len(nums)
    
    # Initialize with first element
    currSum = nums[0]
    maxSum = nums[0]

    
    # Python: Start from index 1, iterate through array
    for i in range(1, arrLen):
        
        # Add current element to running sum
        currSum = currSum + nums[i]
        
        # Reset sum if it becomes negative (start new subarray)
        if currSum < 0:
            currSum = 0
        
        # Python: Built-in max() to track maximum sum seen so far
        maxSum = max(maxSum, currSum)

    return maxSum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))

arr = [1]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))

arr = [5,4,-1,7,8]
print('Max Sum of Sub Array is', maxSumOfSubArray(arr))
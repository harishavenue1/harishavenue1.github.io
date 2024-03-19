def threeSumEqZero(nums):
    leftIndex = 0
    rightIndex = len(nums) - 1
    sum = 0

    # set to store all possible values
    valuesList = list()

    # sort
    nums.sort()

    for i in range(len(nums)):
        leftIndex = i+1
        while leftIndex < rightIndex:
            sum = nums[i] + nums[leftIndex] + nums[rightIndex]
            if sum > 0:
                rightIndex = rightIndex - 1
            elif sum < 0:
                leftIndex = leftIndex + 1
            else:
                valuesList.append([nums[i], nums[leftIndex], nums[rightIndex]])
                leftIndex = leftIndex + 1
                rightIndex = rightIndex - 1
    
    return list(map(list,set(map(tuple,valuesList))))
    

arr = [-1,0,1,2,-1,-4]
output = threeSumEqZero(arr);
print("List of Values Equals to Zero", output);
def twoSum(nums, target):
    numMap = {}

    for i in range(len(nums)):
        key = target - nums[i]
        if key in numMap:
            return [numMap[key], i]
        numMap[nums[i]] = i

    return []  # No solution found


numsList = [1,2,3,4,5]
targetNum = 9
print(twoSum(numsList, targetNum)) # return index of twosum=target

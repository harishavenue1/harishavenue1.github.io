def twoSum(nums, target):
    
    # Python: Dictionary {} to store number -> index mapping for O(1) lookup
    numMap = {}

    
    # Python: range(len()) for indexed iteration
    for i in range(len(nums)):
        
        # Calculate complement needed to reach target
        key = target - nums[i]
        
        # Python: 'in' operator checks if complement exists in dictionary
        if key in numMap:
            
            # Python: List literal syntax for return
            return [numMap[key], i]
        
        # Python: Dictionary assignment to store current number and index
        numMap[nums[i]] = i

    return []  # No solution found


numsList = [1,2,3,4,5]
targetNum = 9
print(twoSum(numsList, targetNum)) # return index of twosum=target

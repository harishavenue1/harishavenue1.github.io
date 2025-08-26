def threeSumEqZero(nums):
    
    # Python: Initialize pointers and sum variable
    leftIndex = 0
    rightIndex = len(nums) - 1
    sum = 0

    
    # Python: List to store all possible triplets
    valuesList = list()

    
    # Python: Built-in sort() for array sorting
    nums.sort()

    
    # Python: Outer loop fixes first element of triplet
    for i in range(len(nums)):
        
        # Start after current element
        leftIndex = i+1
        
        # Python: Two-pointer approach for remaining two elements
        while leftIndex < rightIndex:
            sum = nums[i] + nums[leftIndex] + nums[rightIndex]
            
            if sum > 0:
                
                # Decrease sum (array is sorted)
                rightIndex = rightIndex - 1
            elif sum < 0:
                
                # Increase sum
                leftIndex = leftIndex + 1
            else:
                
                # Found triplet that sums to zero
                valuesList.append([nums[i], nums[leftIndex], nums[rightIndex]])
                leftIndex = leftIndex + 1
                rightIndex = rightIndex - 1
    
    
    # Python: Remove duplicates using set/tuple conversion
    return list(map(list,set(map(tuple,valuesList))))
    

arr = [-1,0,1,2,-1,-4]
output = threeSumEqZero(arr);
print("List of Values Equals to Zero", output);
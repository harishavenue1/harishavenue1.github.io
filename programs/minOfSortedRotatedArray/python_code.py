def findMin_sorted_rotatedArray(nums):
    
    # Python: Tuple unpacking for binary search pointers
    leftIndex, rightIndex = 0, len(nums) - 1
    midIndex = 0

    
    # Python: Modified binary search to find minimum
    while (leftIndex < rightIndex - 1):
        
        # Python: Floor division // for integer division
        midIndex = (leftIndex + rightIndex) // 2
        
        # Python: Compare middle with right to determine which half to search
        if (nums[midIndex] < nums[rightIndex]):
            rightIndex = midIndex  # Minimum is in left half
        else:
            leftIndex = midIndex   # Minimum is in right half

    
    # Python: Conditional expression to return smaller element
    return nums[leftIndex] if nums[leftIndex] < nums[rightIndex] else nums[rightIndex]

arr = [3,4,5,1,2]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)

arr = [4,5,6,7,0,1,2]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)

arr = [11,13,15,17]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)

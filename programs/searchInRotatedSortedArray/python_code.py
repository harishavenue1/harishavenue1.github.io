def searchInRotatedSortedArray(nums, target):
  
  # Python: Binary search pointers for rotated array
  leftIndex, rightIndex = 0, len(nums)-1
  midIndex = 0
  
  
  # Python: Modified binary search for rotated array
  while (leftIndex < rightIndex - 1):
    
    # Python: Floor division // for integer division
    midIndex = (leftIndex + rightIndex) // 2
    
    # Python: Check if target found
    if nums[midIndex] == target:
      return midIndex
    elif nums[midIndex] > target:
      leftIndex = midIndex
    else:
      rightIndex = midIndex
      
  
  # Python: Return -1 if target not found
  return -1
  
arr = [4,5,6,7,0,1,2]
target = 0
targetIndex = searchInRotatedSortedArray(arr, target)
print("Target index is", targetIndex)

target = 3
targetIndex = searchInRotatedSortedArray(arr, target)
print("Target index is", targetIndex)

arr = [1]
target = 0
targetIndex = searchInRotatedSortedArray(arr, target)
print("Target index is", targetIndex)

def searchInRotatedSortedArray(nums, target):
  leftIndex, rightIndex = 0, len(nums)-1
  midIndex = 0
  
  while (leftIndex < rightIndex - 1):
    midIndex = (leftIndex + rightIndex) // 2
    if nums[midIndex] == target:
      return midIndex
    elif nums[midIndex] > target:
      leftIndex = midIndex
    else:
      rightIndex = midIndex
      
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

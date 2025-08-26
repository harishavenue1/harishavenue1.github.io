searchInRotatedSortedArray = function(nums, target) {
  
  // JavaScript: Binary search pointers for rotated array
  let leftIndex = 0
  let rightIndex = nums.length-1
  let midIndex = 0
  
  
  // JavaScript: Modified binary search for rotated array
  while (leftIndex < rightIndex - 1) 
  {
    
    // JavaScript: Math.floor() for integer division
    midIndex = Math.floor((leftIndex + rightIndex) / 2)
    
    // JavaScript: Check if target found
    if (nums[midIndex] == target)
      return midIndex
    else if(nums[midIndex] > target)
      leftIndex = midIndex
    else
      rightIndex = midIndex
  }
      
  
  // JavaScript: Return -1 if target not found
  return -1
};
  
let arr = [4,5,6,7,0,1,2]
let target = 0
let targetIndex = searchInRotatedSortedArray(arr, target)
console.log("Target index is "+ targetIndex)

target = 3
targetIndex = searchInRotatedSortedArray(arr, target)
console.log("Target index is "+ targetIndex)

arr = [1]
target = 0
targetIndex = searchInRotatedSortedArray(arr, target)
console.log("Target index is "+ targetIndex)

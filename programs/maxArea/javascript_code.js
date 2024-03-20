findMaxArea = function(heights) {
  let leftIndex = 0
  let rightIndex = heights.length-1
  let height = 0
  let width = 0
  let maxArea = 0
  
  while (leftIndex < rightIndex) 
  {
    width = rightIndex - leftIndex
    height = Math.min(heights[leftIndex], heights[rightIndex])
    maxArea = Math.max(maxArea, height*width)
    
    if (heights[leftIndex] > heights[rightIndex])
      rightIndex--
    else if (heights[leftIndex] < heights[rightIndex])
      leftIndex++
    else {
      leftIndex++
      rightIndex--
    }
  }
    
  return maxArea
};
  
arr = [1,8,6,2,5,4,8,3,7]
maxArea = findMaxArea(arr)
console.log("Max Area is", maxArea)

arr = [1,1]
maxArea = findMaxArea(arr)
console.log("Max Area is", maxArea)

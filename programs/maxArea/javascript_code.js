findMaxArea = function(heights) {
  
  // JavaScript: Two-pointer approach for container with most water
  let leftIndex = 0
  let rightIndex = heights.length-1
  
  // Initialize variables for calculations
  let height = 0
  let width = 0
  let maxArea = 0
  
  
  // JavaScript: while loop until pointers meet
  while (leftIndex < rightIndex) 
  {
    
    // Calculate current container dimensions
    width = rightIndex - leftIndex
    
    // JavaScript: Math.min() finds limiting height
    height = Math.min(heights[leftIndex], heights[rightIndex])
    
    // JavaScript: Math.max() tracks maximum area
    maxArea = Math.max(maxArea, height*width)
    
    
    // Move pointer with shorter height inward (greedy approach)
    if (heights[leftIndex] > heights[rightIndex])
      rightIndex--
    else if (heights[leftIndex] < heights[rightIndex])
      leftIndex++
    else {
      
      // Equal heights: move both pointers
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

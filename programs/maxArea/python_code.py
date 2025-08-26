def findMaxArea(heights):
  
  # Python: Two-pointer approach for container with most water
  leftIndex = 0
  rightIndex = len(heights)-1
  
  # Python: Multiple assignment for initialization
  height, width, maxArea = 0, 0, 0
  
  
  # Python: while loop until pointers meet
  while leftIndex < rightIndex:
    
    # Calculate current container dimensions
    width = rightIndex - leftIndex
    
    # Python: Built-in min() function finds limiting height
    height = min(heights[leftIndex], heights[rightIndex])
    
    # Python: Built-in max() function tracks maximum area
    maxArea = max(maxArea, height*width)
    
    
    # Move pointer with shorter height inward (greedy approach)
    if heights[leftIndex] > heights[rightIndex]:
      rightIndex -= 1
    elif heights[leftIndex] < heights[rightIndex]:
      leftIndex += 1
    else:
      
      # Equal heights: move both pointers
      leftIndex += 1
      rightIndex -= 1
    
  return maxArea
  
arr = [1,8,6,2,5,4,8,3,7]
maxArea = findMaxArea(arr)
print("Max Area is", maxArea)

arr = [1,1]
maxArea = findMaxArea(arr)
print("Max Area is", maxArea)

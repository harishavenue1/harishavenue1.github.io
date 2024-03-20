def findMaxArea(heights):
  leftIndex = 0
  rightIndex = len(heights)-1
  height, width, maxArea = 0, 0, 0
  
  while leftIndex < rightIndex:
    width = rightIndex - leftIndex
    height = min(heights[leftIndex], heights[rightIndex])
    maxArea = max(maxArea, height*width)
    
    if heights[leftIndex] > heights[rightIndex]:
      rightIndex -= 1
    elif heights[leftIndex] < heights[rightIndex]:
      leftIndex += 1
    else:
      leftIndex += 1
      rightIndex -= 1
    
  return maxArea
  
arr = [1,8,6,2,5,4,8,3,7]
maxArea = findMaxArea(arr)
print("Max Area is", maxArea)

arr = [1,1]
maxArea = findMaxArea(arr)
print("Max Area is", maxArea)

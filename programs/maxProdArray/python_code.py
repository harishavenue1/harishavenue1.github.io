def maxProduct(nums):
  
  # Python: Initialize max product with first element
  maxProd = nums[0]
  
  # Python: Tuple unpacking for left and right products
  leftProd, rightProd = 1, 1
  
  # Python: Get array length
  arrLen = len(nums)
  
  
  # Python: Single pass from both directions
  for i in range(arrLen):
    
    
    # Python: Reset to 1 if product becomes 0 (conditional expression)
    leftProd = 1 if leftProd == 0 else leftProd
    rightProd = 1 if rightProd == 0 else rightProd
    
    
    # Python: Calculate products from left and right
    leftProd = leftProd * nums[i]
    rightProd = rightProd * nums[arrLen - 1 - i]
    
    
    # Python: Built-in max() to track maximum product
    maxProd = max(maxProd, max(leftProd, rightProd))
  
  return maxProd
  
arr = [2,3,-2,4]
print('maxProd is', maxProduct(arr))

arr = [-2,0,-1]
print('maxProd is', maxProduct(arr))

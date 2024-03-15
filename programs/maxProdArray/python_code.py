def maxProduct(nums):
  maxProd = nums[0] #default
  leftProd, rightProd = 1, 1
  arrLen = len(nums)
  
  for i in range(arrLen):
    
    leftProd = 1 if leftProd == 0 else leftProd
    rightProd = 1 if rightProd == 0 else rightProd
    
    leftProd = leftProd * nums[i]
    rightProd = rightProd * nums[arrLen - 1 - i]
    
    maxProd = max(maxProd, max(leftProd, rightProd))
  
  return maxProd
  
arr = [2,3,-2,4]
print('maxProd is', maxProduct(arr))

arr = [-2,0,-1]
print('maxProd is', maxProduct(arr))

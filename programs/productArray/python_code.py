def productArray(nums):
  
  # Python: Two-pass algorithm for product of array except self
  num_len = len(nums)
  
  # Python: List multiplication to create array of 1s
  answer = [1] * num_len
  
  # Python: Tuple unpacking for prefix and postfix products
  pre, post = 1, 1
  
  
  # First pass: calculate prefix products (left to right)
  for i in range(num_len):
    
    # Store product of all elements to the left
    answer[i] = pre
    
    # Update prefix product
    pre = pre * nums[i]
    
  
  # Second pass: multiply by postfix products (right to left)
  for i in range(num_len-1, -1, -1):
    
    # Multiply by product of all elements to the right
    answer[i] = answer[i] * post
    
    # Update postfix product
    post = post * nums[i]
    
  return answer
  
arr = [1,2,3,4]
newArr = productArray(arr)
print('productArray', newArr)

arr = [-1,1,0,-3,3]
newArr = productArray(arr)
print('productArray', newArr)

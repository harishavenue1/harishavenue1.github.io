def productArray(nums):
  num_len = len(nums)
  answer = [1] * num_len
  pre, post = 1, 1
  
  for i in range(num_len):
    answer[i] = pre
    pre = pre * nums[i]
    
  for i in range(num_len-1, -1, -1):
    answer[i] = answer[i] * post
    post = post * nums[i]
    
  return answer
  
arr = [1,2,3,4]
newArr = productArray(arr)
print('productArray', newArr)

arr = [-1,1,0,-3,3]
newArr = productArray(arr)
print('productArray', newArr)

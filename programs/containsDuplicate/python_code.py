def containsDuplicate(nums):
  inSet = set()
  for i in nums:
    if i in inSet:
      return True
    inSet.add(i)
  return False
  
print('containsDuplicate', containsDuplicate([1,2,3,1]))
print('containsDuplicate', containsDuplicate([1,2,3,4]))
print('containsDuplicate', containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
  

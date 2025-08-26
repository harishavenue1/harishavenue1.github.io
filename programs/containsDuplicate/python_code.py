def containsDuplicate(nums):
  
  # Python: set() for O(1) average lookup time
  inSet = set()
  
  # Python: Direct iteration over list elements
  for i in nums:
    
    # Python: 'in' operator checks membership in set
    if i in inSet:
      return True
      
    # Python: .add() method adds element to set
    inSet.add(i)
    
  return False  # No duplicates found
  
print('containsDuplicate', containsDuplicate([1,2,3,1]))
print('containsDuplicate', containsDuplicate([1,2,3,4]))
print('containsDuplicate', containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
  

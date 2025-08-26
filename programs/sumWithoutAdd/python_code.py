def sumWithoutAdd(a, b):
  
  # Python: Temporary variable for XOR calculation
  temp = 0
  
  
  # Python: Loop until no carry bits remain
  while a != 0:
    
    # Python: XOR operation for sum without carry
    temp = a ^ b
    
    # Python: Calculate carry using AND and left shift
    a = (a & b) << 1
    
    # Update sum for next iteration
    b = temp
  
  return b

a, b = 1, 2
print('Sum of A & B is', sumWithoutAdd(a, b))

a, b = 3, 2
print('Sum of A & B is', sumWithoutAdd(a, b))

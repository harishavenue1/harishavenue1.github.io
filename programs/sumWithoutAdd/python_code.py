def sumWithoutAdd(a, b):
  temp = 0
  
  while a != 0:
    temp = a ^ b
    a = (a & b) << 1
    b = temp
  
  return b

a, b = 1, 2
print('Sum of A & B is', sumWithoutAdd(a, b))

a, b = 3, 2
print('Sum of A & B is', sumWithoutAdd(a, b))

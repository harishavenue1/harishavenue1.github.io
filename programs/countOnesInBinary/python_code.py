def bitWiseAndCount(num):
  
  # Python: Counter for set bits (1s)
  setBit = 0
  
  
  # Python: Loop until all bits are processed
  while num != 0:
    
    # Python: AND with 1 to check if least significant bit is 1
    setBit += num & 1
    
    # Python: Right shift to process next bit
    num = num >> 1
    
  print('Set Bit', setBit)
  
  
bitWiseAndCount(11)
bitWiseAndCount(128)
bitWiseAndCount(2147483645)

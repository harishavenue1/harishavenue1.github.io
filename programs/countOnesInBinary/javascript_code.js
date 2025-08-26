bitWiseAndCount = function(num) {
  
  // JavaScript: Counter for set bits (1s)
  let setBit = 0
  
  
  // JavaScript: Loop until all bits are processed
  while (num != 0) {
    
    // JavaScript: AND with 1 to check if least significant bit is 1
    setBit += num & 1
    
    // JavaScript: Right shift to process next bit
    num = num >> 1
  }
    
  console.log('Set Bit', setBit)
};
  
bitWiseAndCount(11)
bitWiseAndCount(128)
bitWiseAndCount(2147483645)

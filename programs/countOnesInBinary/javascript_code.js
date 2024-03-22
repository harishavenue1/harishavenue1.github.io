bitWiseAndCount = function(num) {
  let setBit = 0
  
  while (num != 0) {
    setBit += num & 1 
    num = num >> 1
  }
    
  console.log('Set Bit', setBit)
};
  
bitWiseAndCount(11)
bitWiseAndCount(128)
bitWiseAndCount(2147483645)

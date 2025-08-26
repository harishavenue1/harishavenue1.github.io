sumWithoutAdd = function(a, b) {
  
  // JavaScript: Temporary variable for XOR calculation
  let temp = 0
  
  
  // JavaScript: Loop until no carry bits remain
  while (a != 0) {
    
    // JavaScript: XOR operation for sum without carry
    temp = a ^ b
    
    // JavaScript: Calculate carry using AND and left shift
    a = (a & b) << 1
    
    // Update sum for next iteration
    b = temp
  }
  
  return b
};

let a = 1
let b = 2
console.log('Sum of A & B is', sumWithoutAdd(a, b))

a = 3
b = 2
console.log('Sum of A & B is', sumWithoutAdd(a, b))

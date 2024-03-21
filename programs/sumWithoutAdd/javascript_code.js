sumWithoutAdd = function(a, b) {
  let temp = 0
  
  while (a != 0) {
    temp = a ^ b
    a = (a & b) << 1
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

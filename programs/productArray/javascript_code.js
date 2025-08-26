productArray = function (nums) {
  
  // JavaScript: Two-pass algorithm for product of array except self
  let len = nums.length;
  
  // JavaScript: new Array() to create result array
  let answer = new Array(len);
  
  // prefix and postfix products
  let pre = 1, post = 1;
  
  
  // First pass: calculate prefix products (left to right)
  for (let i = 0; i < len; i++) {
    
    // Store product of all elements to the left
    answer[i] = pre;
    
    // Update prefix product
    pre *= nums[i];
  }
  
  
  // Second pass: multiply by postfix products (right to left)
  for (let i = len-1; i >=0; i--) {
    
    // Multiply by product of all elements to the right
    answer[i] *= post;
    
    // Update postfix product
    post *= nums[i];
  }
  
  return answer;
};

let arr = [1,2,3,4];
let newArr = productArray(arr);
console.log('productArray '+ newArr);

arr = [-1,1,0,-3,3];
newArr = productArray(arr);
console.log('productArray '+ newArr);

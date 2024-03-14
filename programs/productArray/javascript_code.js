productArray = function (nums) {
  let len = nums.length;
  let answer = new Array(len);
  let pre = 1, post = 1;
  
  for (let i = 0; i < len; i++) {
    answer[i] = pre;
    pre *= nums[i];
  }
  
  for (let i = len-1; i >=0; i--) {
    answer[i] *= post;
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

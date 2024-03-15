maxProduct = function (nums) {
    let maxProd = nums[0];
    let leftProd = 1, rightProd = 1;
    let arrLen = nums.length;

    for (let i=0; i<arrLen; i++) {

        // reset prodValues to 1 if value goes to 0
        leftProd = (leftProd == 0? 1 : leftProd)
        rightProd = (rightProd == 0? 1 : rightProd)

        leftProd *= nums[i]
        rightProd *= nums[arrLen - 1 - i]

        maxProd = Math.max(maxProd, Math.max(leftProd, rightProd))      
    }
    return maxProd;
};

arr = [2,3,-2,4];
console.log('Max Product is '+ maxProduct(arr));

arr = [-2,0,-1];
console.log('Max Product is '+ maxProduct(arr));

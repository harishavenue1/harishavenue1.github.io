maxProduct = function (nums) {
    
    // JavaScript: Initialize max product with first element
    let maxProd = nums[0];
    
    // JavaScript: Two-direction product calculation
    let leftProd = 1, rightProd = 1;
    
    // JavaScript: Get array length
    let arrLen = nums.length;

    
    // JavaScript: Single pass from both directions
    for (let i=0; i<arrLen; i++) {

        
        // JavaScript: Reset to 1 if product becomes 0 (ternary operator)
        leftProd = (leftProd == 0? 1 : leftProd)
        rightProd = (rightProd == 0? 1 : rightProd)

        
        // Calculate products from left and right
        leftProd *= nums[i]
        rightProd *= nums[arrLen - 1 - i]

        
        // JavaScript: Math.max() to track maximum product
        maxProd = Math.max(maxProd, Math.max(leftProd, rightProd))      
    }
    
    return maxProd;
};

arr = [2,3,-2,4];
console.log('Max Product is '+ maxProduct(arr));

arr = [-2,0,-1];
console.log('Max Product is '+ maxProduct(arr));

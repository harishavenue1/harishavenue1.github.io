maxSumOfSubArray = function (nums) {
    
    // JavaScript: Kadane's Algorithm for maximum subarray sum
    let arrLen = nums.length;
    
    // Initialize with first element
    let currSum = nums[0];
    let maxSum = nums[0];

    
    // JavaScript: Start from index 1, iterate through array
    for (let i = 1; i < arrLen; i++) {
        
        // Add current element to running sum
        currSum += nums[i];
        
        // Reset sum if it becomes negative (start new subarray)
        if (currSum < 0)
            currSum = 0;
        
        // JavaScript: Math.max() to track maximum sum seen so far
        maxSum = Math.max(maxSum, currSum);
    }
    
    return maxSum;
};

let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log('Max Sum of Sub Array ' + maxSumOfSubArray(arr));

arr = [1];
console.log('Max Sum of Sub Array ' + maxSumOfSubArray(arr));

arr = [5, 4, -1, 7, 8];
console.log('Max Sum of Sub Array ' + maxSumOfSubArray(arr));
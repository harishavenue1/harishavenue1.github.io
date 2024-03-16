maxSumOfSubArray = function (nums) {
    let arrLen = nums.length;
    let currSum = nums[0];
    let maxSum = nums[0];

    for (let i = 1; i < arrLen; i++) {
        currSum += nums[i];
        if (currSum < 0)
            currSum = 0;
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
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSeq = function (nums) {
    
    // JavaScript: Get array length
    let arrLen = nums.length
    
    // JavaScript: Create DP array with .fill(1) - each element forms sequence of length 1
    let dp = new Array(arrLen).fill(1)

    
    // JavaScript: Fill DP table using nested loops
    for (let i = 1; i < arrLen; i++) {
        for (let j = 0; j < i; j++) {
            
            // JavaScript: Check if current element can extend previous sequence
            if (nums[i] > nums[j])
                
                // JavaScript: Math.max() to update longest sequence ending at i
                dp[i] = Math.max(dp[i], dp[j] + 1)
        }
    }
    
    
    // JavaScript: Spread operator with Math.max() to find overall longest
    return Math.max(...dp)
};
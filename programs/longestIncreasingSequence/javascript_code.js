/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSeq = function (nums) {
    let arrLen = nums.length
    let dp = new Array(arrLen).fill(1)

    for (let i = 1; i < arrLen; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j])
                dp[i] = Math.max(dp[i], dp[j] + 1)
        }
    }
    return Math.max(...dp)
};
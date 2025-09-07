// Kadane's Algorithm for Maximum Subarray Sum
const arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log("Array:", arr);

const maxSum = kadaneAlgorithm(arr);
console.log("Maximum subarray sum:", maxSum);

// With subarray indices
const result = kadaneWithIndices(arr);
console.log(`Max sum: ${result.maxSum}, Start: ${result.start}, End: ${result.end}`);
console.log("Subarray:", arr.slice(result.start, result.end + 1));

// Basic Kadane's Algorithm
function kadaneAlgorithm(arr) {
    if (arr.length === 0) return 0;
    
    let maxSum = arr[0];
    let currentSum = arr[0];
    
    console.log("\nKadane's Algorithm step by step:");
    console.log(`Initial: maxSum=${maxSum}, currentSum=${currentSum}`);
    
    for (let i = 1; i < arr.length; i++) {
        // Either extend the existing subarray or start a new one
        currentSum = Math.max(arr[i], currentSum + arr[i]);
        maxSum = Math.max(maxSum, currentSum);
        
        console.log(`i=${i}, arr[${i}]=${arr[i]}, currentSum=${currentSum}, maxSum=${maxSum}`);
    }
    
    return maxSum;
}

// Kadane's Algorithm with subarray indices
function kadaneWithIndices(arr) {
    if (arr.length === 0) return {maxSum: 0, start: 0, end: 0};
    
    let maxSum = arr[0];
    let currentSum = arr[0];
    let start = 0, end = 0, tempStart = 0;
    
    for (let i = 1; i < arr.length; i++) {
        if (currentSum < 0) {
            currentSum = arr[i];
            tempStart = i;
        } else {
            currentSum += arr[i];
        }
        
        if (currentSum > maxSum) {
            maxSum = currentSum;
            start = tempStart;
            end = i;
        }
    }
    
    return {maxSum, start, end};
}

// Alternative functional approach using reduce
function kadaneFunctional(arr) {
    if (arr.length === 0) return 0;
    
    const result = arr.reduce((acc, current, index) => {
        const newCurrentSum = Math.max(current, acc.currentSum + current);
        const newMaxSum = Math.max(acc.maxSum, newCurrentSum);
        
        console.log(`Functional i=${index}, current=${current}, currentSum=${newCurrentSum}, maxSum=${newMaxSum}`);
        
        return {
            maxSum: newMaxSum,
            currentSum: newCurrentSum
        };
    }, {maxSum: arr[0], currentSum: arr[0]});
    
    return result.maxSum;
}

console.log("\nFunctional approach:");
const functionalResult = kadaneFunctional(arr);
console.log("Functional result:", functionalResult);

// Handle all negative numbers case
function kadaneAllNegative(arr) {
    if (arr.length === 0) return 0;
    
    // If all numbers are negative, return the maximum single element
    const allNegative = arr.every(num => num < 0);
    if (allNegative) {
        return Math.max(...arr);
    }
    
    return kadaneAlgorithm(arr);
}

const negativeArr = [-5, -2, -8, -1, -4];
console.log("\nAll negative array:", negativeArr);
console.log("Max sum (all negative):", kadaneAllNegative(negativeArr));
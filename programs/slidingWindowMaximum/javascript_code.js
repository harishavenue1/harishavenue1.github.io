// Sliding Window Maximum Sum
const arr = [1, 3, -1, -3, 5, 3, 6, 7];
const windowSize = 3;

console.log("Array:", arr);
console.log("Window size:", windowSize);

const maxSum = slidingWindowMaxSum(arr, windowSize);
console.log("\nMaximum sum of any window:", maxSum);

// Sliding Window Maximum Sum - O(n) optimized
function slidingWindowMaxSum(arr, k) {
    const n = arr.length;
    
    // Calculate first window sum
    let windowSum = 0;
    for (let i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    let maxSum = windowSum;
    console.log("\n=== SLIDING WINDOW MAXIMUM SUM ===");
    console.log(`Window [0-${k - 1}]: Sum = ${windowSum}`);
    
    // Slide the window
    for (let i = k; i < n; i++) {
        windowSum = windowSum - arr[i - k] + arr[i]; // Remove left, add right
        process.stdout.write(`Window [${i - k + 1}-${i}]: Sum = ${windowSum}`);
        
        if (windowSum > maxSum) {
            maxSum = windowSum;
            process.stdout.write(" <- NEW MAX!");
        }
        console.log();
    }
    
    return maxSum;
}
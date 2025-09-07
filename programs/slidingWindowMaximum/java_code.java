import java.util.Arrays;

public class java_code {
    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int windowSize = 3;
        
        System.out.println("Array: " + Arrays.toString(arr));
        System.out.println("Window size: " + windowSize);
        
        int maxSum = slidingWindowMaxSum(arr, windowSize);
        System.out.println("\nMaximum sum of any window: " + maxSum);
    }
    
    // Sliding Window Maximum Sum - O(n) optimized
    public static int slidingWindowMaxSum(int[] arr, int k) {
        int n = arr.length;
        
        // Calculate first window sum
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        
        int maxSum = windowSum;
        System.out.println("\n=== SLIDING WINDOW MAXIMUM SUM ===");
        System.out.printf("Window [0-%d]: Sum = %d\n", k - 1, windowSum);
        
        // Slide the window
        for (int i = k; i < n; i++) {
            windowSum = windowSum - arr[i - k] + arr[i]; // Remove left, add right
            System.out.printf("Window [%d-%d]: Sum = %d", i - k + 1, i, windowSum);
            
            if (windowSum > maxSum) {
                maxSum = windowSum;
                System.out.print(" <- NEW MAX!");
            }
            System.out.println();
        }
        
        return maxSum;
    }
}
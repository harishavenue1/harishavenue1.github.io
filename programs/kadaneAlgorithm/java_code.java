import java.util.Arrays;

public class java_code {
    public static void main(String[] args) {
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Array: " + Arrays.toString(arr));
        
        int maxSum = kadaneAlgorithm(arr);
        System.out.println("Maximum subarray sum: " + maxSum);
        
        // With subarray indices
        int[] result = kadaneWithIndices(arr);
        System.out.println("Max sum: " + result[0] + ", Start: " + result[1] + ", End: " + result[2]);
        System.out.println("Subarray: " + Arrays.toString(Arrays.copyOfRange(arr, result[1], result[2] + 1)));
    }
    
    // Basic Kadane's Algorithm
    public static int kadaneAlgorithm(int[] arr) {
        if (arr.length == 0) return 0;
        
        int maxSum = arr[0];
        int currentSum = arr[0];
        
        System.out.println("\nKadane's Algorithm step by step:");
        System.out.printf("Initial: maxSum=%d, currentSum=%d\n", maxSum, currentSum);
        
        for (int i = 1; i < arr.length; i++) {
            // Either extend the existing subarray or start a new one
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
            
            System.out.printf("i=%d, arr[%d]=%d, currentSum=%d, maxSum=%d\n", 
                i, i, arr[i], currentSum, maxSum);
        }
        
        return maxSum;
    }
    
    // Kadane's Algorithm with subarray indices
    public static int[] kadaneWithIndices(int[] arr) {
        if (arr.length == 0) return new int[]{0, 0, 0};
        
        int maxSum = arr[0];
        int currentSum = arr[0];
        int start = 0, end = 0, tempStart = 0;
        
        for (int i = 1; i < arr.length; i++) {
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
        
        return new int[]{maxSum, start, end};
    }
}
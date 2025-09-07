using System;

class SlidingWindowMaximum
{
    static void Main()
    {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int windowSize = 3;
        
        Console.WriteLine($"Array: [{string.Join(", ", arr)}]");
        Console.WriteLine($"Window size: {windowSize}");
        
        int maxSum = SlidingWindowMaxSum(arr, windowSize);
        Console.WriteLine($"\nMaximum sum of any window: {maxSum}");
    }
    
    // Sliding Window Maximum Sum - O(n) optimized
    static int SlidingWindowMaxSum(int[] arr, int k)
    {
        int n = arr.Length;
        
        // Calculate first window sum
        int windowSum = 0;
        for (int i = 0; i < k; i++)
        {
            windowSum += arr[i];
        }
        
        int maxSum = windowSum;
        Console.WriteLine("\n=== SLIDING WINDOW MAXIMUM SUM ===");
        Console.WriteLine($"Window [0-{k - 1}]: Sum = {windowSum}");
        
        // Slide the window
        for (int i = k; i < n; i++)
        {
            windowSum = windowSum - arr[i - k] + arr[i]; // Remove left, add right
            Console.Write($"Window [{i - k + 1}-{i}]: Sum = {windowSum}");
            
            if (windowSum > maxSum)
            {
                maxSum = windowSum;
                Console.Write(" <- NEW MAX!");
            }
            Console.WriteLine();
        }
        
        return maxSum;
    }
}
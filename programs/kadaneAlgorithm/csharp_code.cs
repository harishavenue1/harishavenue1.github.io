using System;
using System.Linq;

class KadaneAlgorithm
{
    static void Main()
    {
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        Console.WriteLine($"Array: [{string.Join(", ", arr)}]");
        
        int maxSum = KadaneAlgorithm(arr);
        Console.WriteLine($"Maximum subarray sum: {maxSum}");
        
        // With subarray indices
        var result = KadaneWithIndices(arr);
        Console.WriteLine($"Max sum: {result.maxSum}, Start: {result.start}, End: {result.end}");
        Console.WriteLine($"Subarray: [{string.Join(", ", arr.Skip(result.start).Take(result.end - result.start + 1))}]");
    }
    
    // Basic Kadane's Algorithm
    static int KadaneAlgorithm(int[] arr)
    {
        if (arr.Length == 0) return 0;
        
        int maxSum = arr[0];
        int currentSum = arr[0];
        
        Console.WriteLine("\nKadane's Algorithm step by step:");
        Console.WriteLine($"Initial: maxSum={maxSum}, currentSum={currentSum}");
        
        for (int i = 1; i < arr.Length; i++)
        {
            // Either extend the existing subarray or start a new one
            currentSum = Math.Max(arr[i], currentSum + arr[i]);
            maxSum = Math.Max(maxSum, currentSum);
            
            Console.WriteLine($"i={i}, arr[{i}]={arr[i]}, currentSum={currentSum}, maxSum={maxSum}");
        }
        
        return maxSum;
    }
    
    // Kadane's Algorithm with subarray indices
    static (int maxSum, int start, int end) KadaneWithIndices(int[] arr)
    {
        if (arr.Length == 0) return (0, 0, 0);
        
        int maxSum = arr[0];
        int currentSum = arr[0];
        int start = 0, end = 0, tempStart = 0;
        
        for (int i = 1; i < arr.Length; i++)
        {
            if (currentSum < 0)
            {
                currentSum = arr[i];
                tempStart = i;
            }
            else
            {
                currentSum += arr[i];
            }
            
            if (currentSum > maxSum)
            {
                maxSum = currentSum;
                start = tempStart;
                end = i;
            }
        }
        
        return (maxSum, start, end);
    }
}
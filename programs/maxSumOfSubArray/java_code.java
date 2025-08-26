
class java_code 
{
    public static void main(String[] args) 
    {
        int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println("Max Sum of Sub Array " + maxSumOfSubArray(arr));

        arr = new int[] { 1 };
        System.out.println("Max Sum of Sub Array " + maxSumOfSubArray(arr));

        arr = new int[] { 5, 4, -1, 7, 8 };
        System.out.println("Max Sum of Sub Array " + maxSumOfSubArray(arr));
    }

    public static int maxSumOfSubArray(int[] nums) 
    {
        
        // Java: Kadane's Algorithm for maximum subarray sum
        int arrLen = nums.length;
        
        // Initialize with first element
        int currSum = nums[0];
        int maxSum = nums[0];

        
        // Java: Start from index 1, iterate through array
        for (int i = 1; i < arrLen; i++) 
        {
            
            // Add current element to running sum
            currSum += nums[i];
            
            // Reset sum if it becomes negative (start new subarray)
            if (currSum < 0)
                currSum = 0;
            
            // Java: Math.max() to track maximum sum seen so far
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }
}

public class Solution
{
    public int longestSeq(int[] nums)
    {
        
        // C#: Handle edge cases
        if (nums == null || nums.Length == 0)
        {
            return 0;
        }

        
        // C#: Get array length
        int n = nums.Length;
        
        // C#: DP array with Array.Fill(1) - each element forms sequence of length 1
        int[] dp = new int[n];
        Array.Fill(dp, 1);

        
        // C#: Fill DP table using nested loops
        for (int i = 1; i < n; ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                
                // C#: Check if current element can extend previous sequence
                if (nums[i] > nums[j])
                {
                    
                    // C#: Math.Max() to update longest sequence ending at i
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
        }

        
        // C#: LINQ .Max() to find overall longest sequence
        int maxLength = dp.Max();
        return maxLength;
    }
}
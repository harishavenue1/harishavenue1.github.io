public class Solution
{
    public int LongestCommonSubsequence(string s1, string s2)
    {
        
        // C#: Get string lengths using .Length property
        int len1 = s1.Length;
        int len2 = s2.Length;

        
        // C#: 2D array declaration with comma syntax
        int[,] dp = new int[len1 + 1, len2 + 1];

        
        // C#: Nested loops to fill DP table
        for (int i = 1; i <= len1; i++)
        {
            for (int j = 1; j <= len2; j++)
            {
                
                // C#: Direct character comparison using indexing
                if (s1[i - 1] == s2[j - 1])
                    dp[i, j] = 1 + dp[i - 1, j - 1];  // Characters match
                else
                    
                    // C#: Math.Max() for maximum value
                    dp[i, j] = Math.Max(dp[i, j - 1], dp[i - 1, j]);
            }
        }
        
        return dp[len1, len2];
    }
}
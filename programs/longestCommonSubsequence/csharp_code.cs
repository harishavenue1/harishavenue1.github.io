public class Solution
{
    public int LongestCommonSubsequence(string s1, string s2)
    {
        int len1 = s1.Length;
        int len2 = s2.Length;

        int[,] dp = new int[len1 + 1, len2 + 1];

        for (int i = 1; i <= len1; i++)
        {
            for (int j = 1; j <= len2; j++)
            {
                if (s1[i - 1] == s2[j - 1])
                    dp[i, j] = 1 + dp[i - 1, j - 1];
                else
                    dp[i, j] = Math.Max(dp[i, j - 1], dp[i - 1, j]);
            }
        }
        return dp[len1, len2];
    }
}
public class Solution
{
    public int longestSeq(int[] nums)
    {
        if (nums == null || nums.Length == 0)
        {
            return 0;
        }

        int n = nums.Length;
        int[] dp = new int[n];
        Array.Fill(dp, 1);

        for (int i = 1; i < n; ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (nums[i] > nums[j])
                {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxLength = dp.Max();
        return maxLength;
    }
}
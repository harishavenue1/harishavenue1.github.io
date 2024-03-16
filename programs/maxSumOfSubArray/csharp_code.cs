using System;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
            Console.WriteLine("Max Sum of Sub Array " + maxSumOfSubArray(arr));

            arr = new int[] { 1 };
            Console.WriteLine("Max Sum of Sub Array " + maxSumOfSubArray(arr));

            arr = new int[] { 5, 4, -1, 7, 8 };
            Console.WriteLine("Max Sum of Sub Array " + maxSumOfSubArray(arr));
        }

        public static int maxSumOfSubArray(int[] nums)
        {
            int arrLen = nums.Length;
            int currSum = nums[0];
            int maxSum = nums[0];

            for (int i = 1; i < arrLen; i++)
            {
                currSum += nums[i];
                if (currSum < 0)
                    currSum = 0;
                maxSum = Math.Max(maxSum, currSum);
            }
            return maxSum;
        }
    }
}
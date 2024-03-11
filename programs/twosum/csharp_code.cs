using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int[] output = TwoSum(new int[] { 1, 2, 3, 4, 5 }, 9);
        Console.WriteLine(string.Join(",", output));
    }
    public static int[] TwoSum(int[] nums, int target)
    {
        if (nums == null || nums.Length < 2)
            return new int[2];

        Dictionary<int, int> check = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if (check.ContainsKey(target - nums[i]))
            {
                return new int[] { check[target - nums[i]], i };
            }
            check[nums[i]] = i;
        }
        return new int[] { 0, 0 };
    }
}
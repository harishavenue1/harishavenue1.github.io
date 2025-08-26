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
        
        // C#: Input validation with null check and .Length property
        if (nums == null || nums.Length < 2)
            return new int[2];

        
        // C#: Dictionary<TKey, TValue> to store number -> index mapping
        Dictionary<int, int> check = new Dictionary<int, int>();

        
        // C#: Standard for-loop with .Length property (capital L)
        for (int i = 0; i < nums.Length; i++)
        {
            
            // C#: .ContainsKey() checks if complement exists in dictionary
            if (check.ContainsKey(target - nums[i]))
            {
                
                // C#: Array initialization syntax for return
                return new int[] { check[target - nums[i]], i };
            }
            
            // C#: Dictionary indexer to store current number and index
            check[nums[i]] = i;
        }
        return new int[] { 0, 0 };
    }
}
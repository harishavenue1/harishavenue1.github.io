using System;
using System.Linq;

namespace MyCompiler
{
    class Program
    {
        public static void Main(String[] args)
        {
            int[] arr = { 9, 6, 4, 2, 3, 5, 7, 0, 1 };
            missingNum(arr);
            arr = new int[] { 0, 1 };
            missingNum(arr);
            arr = new int[] { 3, 0, 1 };
            missingNum(arr);
        }
        public static void missingNum(int[] nums)
        {
            
            // C#: Get array length using .Length property
            int length = nums.Length;
            
            // C#: Calculate expected sum using arithmetic series formula
            int expected = ((length + 1) * length / 2);
            
            // C#: LINQ .Sum() method for actual sum
            int actual = nums.Sum();
            
            
            // C#: Output missing number (difference between expected and actual)
            Console.WriteLine("Missing Number " + (expected - actual));
        }
    }
}
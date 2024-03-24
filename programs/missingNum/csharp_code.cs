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
            int length = nums.Length;
            int expected = ((length + 1) * length / 2);
            int actual = nums.Sum();
            Console.WriteLine("Missing Number " + (expected - actual));
        }
    }
}
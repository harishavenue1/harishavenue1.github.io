using System;

namespace MyCompiler 
{
    class Program 
    {
        public static void Main(string[] args) 
        {
            int[] arr = {3,4,5,1,2};
            int output = findMin_sorted_rotatedArray(arr);
            Console.WriteLine("Minimum of Sorted and if rotated Array is "+ output);
    
            arr = new int[] {4,5,6,7,0,1,2};
            output = findMin_sorted_rotatedArray(arr);
            Console.WriteLine("Minimum of Sorted and if rotated Array is "+ output);
    
            arr = new int[] {11,13,15,17};
            output = findMin_sorted_rotatedArray(arr);
            Console.WriteLine("Minimum of Sorted and if rotated Array is "+ output);
        }

        public static int findMin_sorted_rotatedArray(int[] nums) 
        {
            
            // C#: Binary search pointers for rotated array
            int leftIndex = 0;
            int midIndex = 0;
            int rightIndex = nums.Length - 1;

            
            // C#: Modified binary search to find minimum
            while (leftIndex < rightIndex - 1) 
            {
                
                // C#: Integer division for middle index
                midIndex = (leftIndex + rightIndex) / 2;
                
                // C#: Compare middle with right to determine which half to search
                if (nums[midIndex] < nums[rightIndex])
                    rightIndex = midIndex;  // Minimum is in left half
                else
                    leftIndex = midIndex;   // Minimum is in right half
            }
            
            
            // C#: Ternary operator to return smaller element
            return (nums[leftIndex] < nums[rightIndex] ? nums[leftIndex] : nums[rightIndex]);
        }
    }
}

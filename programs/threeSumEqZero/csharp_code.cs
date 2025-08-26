using System;
using System.Collections.Generic;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            int[] arr = { -1, 0, 1, 2, -1, -4 };
            List<List<int>> output = threeSumEqZero(arr);
            foreach (var li in output)
            {
                Console.WriteLine("List of Values Equals to Zero " + String.Join(" ", li));
            }
        }

        public static List<List<int>> threeSumEqZero(int[] nums)
        {
            
            // C#: Array.Sort() for array sorting
            Array.Sort(nums);

            
            // C#: HashSet to store unique triplets
            HashSet<List<int>> valuesSet = new HashSet<List<int>>();

            
            // C#: List to store all possible triplets
            List<List<int>> valuesList = new List<List<int>>();

            
            // Initialize variables
            int sum = 0, leftIndex = 0, rightIndex = nums.Length - 1;

            
            // C#: Outer loop fixes first element of triplet
            for (int i = 0; i < nums.Length; i++)
            {
                
                // Start after current element
                leftIndex = i + 1;
                
                // C#: Two-pointer approach for remaining two elements
                while (leftIndex < rightIndex)
                {
                    sum = nums[i] + nums[leftIndex] + nums[rightIndex];
                    
                    if (sum > 0)
                        
                        // Decrease sum (array is sorted)
                        rightIndex--;
                    else if (sum < 0)
                        
                        // Increase sum
                        leftIndex++;
                    else
                    {
                        
                        // Found triplet that sums to zero
                        valuesSet.Add(new List<int>(new int[] { nums[i], nums[leftIndex], nums[rightIndex] }));
                        leftIndex++;
                        rightIndex--;
                    }
                }
            }
            
            
            // C#: .AddRange() to convert HashSet to List
            valuesList.AddRange(valuesSet);
            return valuesList;
        }
    }
}
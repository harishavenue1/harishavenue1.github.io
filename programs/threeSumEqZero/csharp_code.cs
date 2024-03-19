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
            // sort the array
            Array.Sort(nums);

            // to store unique values
            HashSet<List<int>> valuesSet = new HashSet<List<int>>();

            // to store all possible values eq = 0
            List<List<int>> valuesList = new List<List<int>>();

            int sum = 0, leftIndex = 0, rightIndex = nums.Length - 1;

            for (int i = 0; i < nums.Length; i++)
            {
                leftIndex = i + 1;
                while (leftIndex < rightIndex)
                {
                    sum = nums[i] + nums[leftIndex] + nums[rightIndex];
                    if (sum > 0)
                        rightIndex--; //array is sorted, so rightIndex has highest value
                    else if (sum < 0)
                        leftIndex++;
                    else
                    {
                        valuesSet.Add(new List<int>(new int[] { nums[i], nums[leftIndex], nums[rightIndex] }));
                        leftIndex++;
                        rightIndex--;
                    }
                }
            }
            valuesList.AddRange(valuesSet);
            return valuesList;
        }
    }
}
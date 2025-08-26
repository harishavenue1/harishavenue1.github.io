using System;
using System.Collections.Generic;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			int[] arr = { 1, 2, 3, 1 };
			Console.WriteLine("containsDuplicate " + containsDuplicate(arr));

			arr = new int[] { 1, 2, 3, 4 };
			Console.WriteLine("containsDuplicate " + containsDuplicate(arr));

			arr = new int[] { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 };
			Console.WriteLine("containsDuplicate " + containsDuplicate(arr));
		}

		public static Boolean containsDuplicate(int[] nums)
		{
			
			// C#: HashSet<T> for O(1) average lookup time
			HashSet<int> inSet = new HashSet<int>();
			
			// C#: Standard for-loop with .Length property
			for (int i = 0; i < nums.Length; i++)
			{
				
				// C#: .Contains() method checks if element exists
				if (inSet.Contains(nums[i]))
				{
					return true;  // Duplicate found
				}
				
				// C#: .Add() method adds element to HashSet
				inSet.Add(nums[i]);
			}
			
			return false;  // No duplicates found
		}
	}
}
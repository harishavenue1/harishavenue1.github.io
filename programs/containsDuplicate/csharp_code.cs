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
			HashSet<int> inSet = new HashSet<int>();
			for (int i = 0; i < nums.Length; i++)
			{
				if (inSet.Contains(nums[i]))
				{
					return true;
				}
				inSet.Add(nums[i]);
			}
			return false;
		}
	}
}
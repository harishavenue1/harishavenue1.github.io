using System;

namespace HelloWorld
{
  public class Program
  {
    public static void Main(string[] args)
    {
      int[] arr = { 4, 5, 6, 7, 0, 1, 2 };
      int target = 0;
      int targetIndex = searchInRotatedSortedArray(arr, target);
      Console.WriteLine("Target index is " + targetIndex);

      target = 3;
      targetIndex = searchInRotatedSortedArray(arr, target);
      Console.WriteLine("Target index is " + targetIndex);

      arr = new int[] { 1 };
      target = 0;
      targetIndex = searchInRotatedSortedArray(arr, target);
      Console.WriteLine("Target index is " + targetIndex);
    }

    public static int searchInRotatedSortedArray(int[] nums, int target)
    {
      
      // C#: Binary search pointers for rotated array
      int leftIndex = 0;
      int rightIndex = nums.Length - 1;
      int midIndex = 0;

      
      // C#: Modified binary search for rotated array
      while (leftIndex < rightIndex - 1)
      {
        
        // C#: Integer division for middle index
        midIndex = (leftIndex + rightIndex) / 2;
        
        // C#: Check if target found
        if (nums[midIndex] == target)
          return midIndex;
        else if (nums[midIndex] > target)
          leftIndex = midIndex;
        else
          rightIndex = midIndex;
      }
      
      
      // C#: Return -1 if target not found
      return -1;
    }
  }
}

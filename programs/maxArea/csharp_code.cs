using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			int[] arr = {1,8,6,2,5,4,8,3,7};
      int maxArea = findMaxArea(arr);
      Console.WriteLine("Max Area is "+ maxArea);
      
      arr = new int[] {1,1};
      maxArea = findMaxArea(arr);
      Console.WriteLine("Max Area is "+ maxArea);
		}
		
		public static int findMaxArea(int[] heights) 
    {
      int leftIndex = 0;
      int rightIndex = heights.Length - 1;
      int height = 0, width = 0, maxArea = 0;
      
      while (leftIndex < rightIndex) 
      {
        width = rightIndex - leftIndex;
        height = Math.Min(heights[leftIndex], heights[rightIndex]);
        maxArea = Math.Max(maxArea, width * height);
        
        if (heights[leftIndex] < heights[rightIndex])
          leftIndex++;
        else if (heights[leftIndex] > heights[rightIndex])
          rightIndex--;
        else 
        {
          leftIndex++;
          rightIndex--;
        }
      }
      return maxArea;
    }
	}
}

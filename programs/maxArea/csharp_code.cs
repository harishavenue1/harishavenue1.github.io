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
      int[] arr = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
      int maxArea = findMaxArea(arr);
      Console.WriteLine("Max Area is " + maxArea);

      arr = new int[] { 1, 1 };
      maxArea = findMaxArea(arr);
      Console.WriteLine("Max Area is " + maxArea);
    }

    public static int findMaxArea(int[] heights)
    {
      
      // C#: Two-pointer approach for container with most water
      int leftIndex = 0;
      int rightIndex = heights.Length - 1;
      
      // Initialize variables for calculations
      int height = 0, width = 0, maxArea = 0;

      
      // C#: while loop until pointers meet
      while (leftIndex < rightIndex)
      {
        
        // Calculate current container dimensions
        width = rightIndex - leftIndex;
        
        // C#: Math.Min() finds limiting height
        height = Math.Min(heights[leftIndex], heights[rightIndex]);
        
        // C#: Math.Max() tracks maximum area
        maxArea = Math.Max(maxArea, width * height);

        
        // Move pointer with shorter height inward (greedy approach)
        if (heights[leftIndex] < heights[rightIndex])
          leftIndex++;
        else if (heights[leftIndex] > heights[rightIndex])
          rightIndex--;
        else
        {
          
          // Equal heights: move both pointers
          leftIndex++;
          rightIndex--;
        }
      }
      
      return maxArea;
    }
  }
}

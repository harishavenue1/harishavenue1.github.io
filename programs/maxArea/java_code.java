public class java_code {
    
    public static void main(String[] args) 
    {
      int[] arr = {1,8,6,2,5,4,8,3,7};
      int maxArea = findMaxArea(arr);
      System.out.println("Max Area is "+ maxArea);
      
      arr = new int[] {1,1};
      maxArea = findMaxArea(arr);
      System.out.println("Max Area is "+ maxArea);
    }
    
    public static int findMaxArea(int[] heights) 
    {
      int leftIndex = 0;
      int rightIndex = heights.length - 1;
      int height = 0, width = 0, maxArea = 0;
      
      while (leftIndex < rightIndex) 
      {
        width = rightIndex - leftIndex;
        height = Math.min(heights[leftIndex], heights[rightIndex]);
        maxArea = Math.max(maxArea, width * height);
        
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

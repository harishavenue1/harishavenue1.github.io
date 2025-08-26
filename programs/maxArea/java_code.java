public class java_code {

  public static void main(String[] args) {
    int[] arr = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
    int maxArea = findMaxArea(arr);
    System.out.println("Max Area is " + maxArea);

    arr = new int[] { 1, 1 };
    maxArea = findMaxArea(arr);
    System.out.println("Max Area is " + maxArea);
  }

  public static int findMaxArea(int[] heights) {
    
    // Java: Two-pointer approach for container with most water
    int leftIndex = 0;
    int rightIndex = heights.length - 1;
    int height = 0, width = 0, maxArea = 0;

    // Java: Move pointers inward until they meet
    while (leftIndex < rightIndex) {
      
      // Calculate current container dimensions
      width = rightIndex - leftIndex;
      
      // Java: Math.min() finds limiting height (shorter wall)
      height = Math.min(heights[leftIndex], heights[rightIndex]);
      
      // Java: Math.max() tracks maximum area found so far
      maxArea = Math.max(maxArea, width * height);

      // Move pointer with shorter height inward (greedy approach)
      if (heights[leftIndex] < heights[rightIndex])
        leftIndex++;
      else if (heights[leftIndex] > heights[rightIndex])
        rightIndex--;
      else {

        // Equal heights: move both pointers
        leftIndex++;
        rightIndex--;
      }
    }
    
    return maxArea;
  }

}

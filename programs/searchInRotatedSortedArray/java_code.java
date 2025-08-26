public class java_code {
  public static void main(String[] args) {
    int[] arr = { 4, 5, 6, 7, 0, 1, 2 };
    int target = 0;
    int targetIndex = searchInRotatedSortedArray(arr, target);
    System.out.println("Target index is " + targetIndex);

    target = 3;
    targetIndex = searchInRotatedSortedArray(arr, target);
    System.out.println("Target index is " + targetIndex);

    arr = new int[] { 1 };
    target = 0;
    targetIndex = searchInRotatedSortedArray(arr, target);
    System.out.println("Target index is " + targetIndex);
  }

  public static int searchInRotatedSortedArray(int[] nums, int target) {
    
    // Java: Modified binary search for rotated sorted array
    int leftIndex = 0;
    int rightIndex = nums.length - 1;
    int midIndex = 0;

    // Java: Binary search with rotation handling
    while (leftIndex < rightIndex - 1) {
      
      // Java: Calculate middle index to avoid overflow
      midIndex = (leftIndex + rightIndex) / 2;
      
      // Found target at middle
      if (nums[midIndex] == target)
        return midIndex;
        
      // Determine which half is sorted and search accordingly
      else if (nums[midIndex] > target)
        leftIndex = midIndex;   // Search right half
      else
        rightIndex = midIndex;  // Search left half
    }
    
    return -1;  // Target not found
  }
}

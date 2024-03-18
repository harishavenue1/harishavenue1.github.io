public class java_code
{
    public static void main(String[] args) 
    {
      int[] arr = {4,5,6,7,0,1,2};
      int target = 0;
      int targetIndex = searchInRotatedSortedArray(arr, target);
      System.out.println("Target index is "+ targetIndex);
      
      target = 3;
      targetIndex = searchInRotatedSortedArray(arr, target);
      System.out.println("Target index is "+ targetIndex);
      
      arr = new int[] {1};
      target = 0;
      targetIndex = searchInRotatedSortedArray(arr, target);
      System.out.println("Target index is "+ targetIndex);
  }
  
  public static int searchInRotatedSortedArray(int[] nums, int target) 
  {
    int leftIndex = 0;
    int rightIndex = nums.length - 1;
    int midIndex = 0;
    
    while (leftIndex < rightIndex - 1) 
    {
      midIndex = (leftIndex + rightIndex) / 2;
      if (nums[midIndex] == target)
        return midIndex;
      else if (nums[midIndex] > target)
        leftIndex = midIndex;
      else
        rightIndex = midIndex;
    }
    return -1;
  }
}

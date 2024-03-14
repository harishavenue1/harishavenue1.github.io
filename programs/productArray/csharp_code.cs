using System;

public class Program
{
  public static void Main(string[] args)
  {
    int[] arr = {1,2,3,4};
    int[] prodArr = productArray(arr);
    Console.WriteLine("productArray "+ string.Join(',', prodArr));
    
    arr = new int[] {-1,1,0,-3,3};
    prodArr = productArray(arr);
    Console.WriteLine("productArray "+ string.Join(',', prodArr));
  }
  
  public static int[] productArray(int[] nums) {
    int len = nums.Length;
    int[] answer = new int[len];
    int pre = 1;
    int post = 1;
    
    for (int i=0; i<len; i++) {
      answer[i] = pre;
      pre *= nums[i];
    }
    
    for (int i=len-1; i>=0; i--) {
      answer[i] *= post;
      post *= nums[i];
    }
    
    return answer;
  }
}

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
    
    // C#: Two-pass algorithm for product of array except self
    int len = nums.Length;
    
    // C#: Array initialization with specified size
    int[] answer = new int[len];
    
    // prefix and postfix products
    int pre = 1;
    int post = 1;
    
    
    // First pass: calculate prefix products (left to right)
    for (int i=0; i<len; i++) {
      
      // Store product of all elements to the left
      answer[i] = pre;
      
      // Update prefix product
      pre *= nums[i];
    }
    
    
    // Second pass: multiply by postfix products (right to left)
    for (int i=len-1; i>=0; i--) {
      
      // Multiply by product of all elements to the right
      answer[i] *= post;
      
      // Update postfix product
      post *= nums[i];
    }
    
    return answer;
  }
}

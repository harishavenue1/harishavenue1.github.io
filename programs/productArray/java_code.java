package programs.productArray;

import java.util.Arrays;

public class java_code 
{
  public static void main(String[] args) 
  {
    int[] arr = { 1, 2, 3, 4 };
    int[] prodArray = productExceptSelf(arr);
    System.out.println("Prod Arr -> " + Arrays.toString(prodArray));

    arr = new int[] { -1, 1, 0, -3, 3 };
    prodArray = productExceptSelf(arr);
    System.out.println("Prod Arr -> " + Arrays.toString(prodArray));
  }

  public static int[] productExceptSelf(int[] nums) 
  {
    
    // Java: Two-pass algorithm for product of array except self
    int len = nums.length;
    int[] answer = new int[len];
    
    // prefix and postfix products
    int pre = 1, post = 1;

    
    // First pass: calculate prefix products (left to right)
    for (int i = 0; i < len; i++) 
    {
      
      // Store product of all elements to the left
      answer[i] = pre;
      
      // Update prefix product
      pre *= nums[i];
    }

    
    // Second pass: multiply by postfix products (right to left)
    for (int i = len - 1; i >= 0; i--) 
    {
      
      // Multiply by product of all elements to the right
      answer[i] *= post;
      
      // Update postfix product
      post *= nums[i];
    }
    
    return answer;
  }
}

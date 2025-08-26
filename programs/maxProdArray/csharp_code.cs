using System;

public class Program
{
  public static void Main(string[] args)
  {
    int[] arr = {2, 3, -2, 4};
    Console.WriteLine("Max Product is "+ MaxProduct(arr));
    
    arr = new int[] {-2, 0, -1};
    Console.WriteLine("Max Product is "+ MaxProduct(arr));
  }
  
  public static int MaxProduct(int[] nums)
  {
    int maxProd = nums[0]; //default
    int leftProd = 1, rightProd = 1;
    int arrLen = nums.Length;
    
    for (int i=0; i<arrLen; i++) 
    {

      // reset prod values to 1 if values goes to 0
      leftProd = (leftProd == 0 ? 1 : leftProd);
      rightProd = (rightProd == 0 ? 1 : rightProd);
      
      leftProd *= nums[i];
      rightProd *= nums[arrLen - 1 - i];
      
      maxProd = Math.Max(maxProd, Math.Max(leftProd, rightProd));
    }
    return maxProd;
  }
}

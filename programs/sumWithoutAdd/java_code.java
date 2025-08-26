public class java_code 
{
  public static void main(String[] args) 
  {
    int a = 1, b = 2;
    System.out.println("Sum of A & B is: "+ sumWithoutAdd(a, b));
    
    a = 2; b = 3;
    System.out.println("Sum of A & B is: "+ sumWithoutAdd(a, b));
  }

  public static int sumWithoutAdd(int a, int b) 
  {
    
    // Java: Temporary variable for carry calculation
    int temp = 0;
    
    // Java: Loop until no carry bits remain
    while (b != 0) 
    {
      
      // Java: Calculate carry using AND and left shift
      temp = (a & b) << 1;
      
      // Java: XOR operation for sum without carry
      a = a ^ b;
      
      // Update carry for next iteration
      b = temp;
    }
    
    return a;
  }
}

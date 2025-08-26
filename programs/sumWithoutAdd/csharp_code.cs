using System;

namespace HelloWorld
{
  public class Program
  {
    public static void Main(string[] args)
    {
      int a = 1, b = 2;
      Console.WriteLine("Sum of A & B is: " + sumWithoutAdd(a, b));

      a = 2; b = 3;
      Console.WriteLine("Sum of A & B is: " + sumWithoutAdd(a, b));
    }

    public static int sumWithoutAdd(int a, int b)
    {
      
      // C#: Temporary variable for carry calculation
      int temp = 0;
      
      // C#: Loop until no carry bits remain
      while (b != 0)
      {
        
        // C#: Calculate carry using AND and left shift
        temp = (a & b) << 1;
        
        // C#: XOR operation for sum without carry
        a = a ^ b;
        
        // Update carry for next iteration
        b = temp;
      }
      
      return a;
    }
  }
}

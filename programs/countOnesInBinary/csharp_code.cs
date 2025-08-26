using System;

namespace HelloWorld
{
  public class Program
  {
    public static void Main(String[] args)
    {
      bitWiseAndCount(11);
      bitWiseAndCount(128);
      bitWiseAndCount(2147483645);
    }

    public static void bitWiseAndCount(int num)
    {
      
      // C#: Counter for set bits (1s)
      int setBit = 0;
      
      // C#: Loop until all bits are processed
      while (num != 0)
      {
        
        // C#: AND with 1 to check if least significant bit is 1
        setBit += num & 1;
        
        // C#: Right shift to process next bit
        num = num >> 1;
      }
      
      Console.WriteLine("Set Bit: " + setBit);
    }
  }
}

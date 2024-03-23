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
      int setBit = 0;
      while (num != 0)
      {
        setBit += num & 1;
        num = num >> 1;
      }
      Console.WriteLine("Set Bit: " + setBit);
    }
  }
}

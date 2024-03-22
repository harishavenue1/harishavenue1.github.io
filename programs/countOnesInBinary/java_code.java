import java.util.*;

public class Main 
{
  public static void main(String[] args) 
  {
    bitWiseAndCount(11);
    bitWiseAndCount(128);
    bitWiseAndCount(2147483645);
  }
  
  public static int bitWiseAndCount(int num) 
  {
    int setBit = 0;
    while (num != 0) 
    {
      setBit += num & 1; // and with num = result (1) if digit is 1
      num = num >>> 1; // next move right to get next digit checked from left
    }
    System.out.println("Set Bit: "+ setBit);
    return setBit;
  }
}

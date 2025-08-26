
public class java_code {
  public static void main(String[] args) {
    bitWiseAndCount(11);
    bitWiseAndCount(128);
    bitWiseAndCount(2147483645);
  }

  public static int bitWiseAndCount(int num) {
    
    // Java: Counter for set bits (1s)
    int setBit = 0;
    
    // Java: Loop until all bits are processed
    while (num != 0) {
      
      // Java: AND with 1 to check if least significant bit is 1
      setBit += num & 1;
      
      // Java: Right shift to process next bit
      num = num >> 1;
    }
    
    System.out.println("Set Bit: " + setBit);
    return setBit;
  }
}

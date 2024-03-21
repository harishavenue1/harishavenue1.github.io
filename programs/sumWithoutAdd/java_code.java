public class Main 
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
    int temp = 0;
    while (b != 0) 
    {
      temp = (a & b) << 1; // and oper and carry left 1 
      a = a ^ b; // xor oper 
      b = temp;
    }
    return a;
  }
}

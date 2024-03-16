package programs.containsDuplicate;

import java.util.HashSet;

public class java_code 
{
  public static void main(String[] args) 
  {
    boolean flag = containsDuplicate(new int[] { 1, 2, 3, 1 });
    System.out.println("containsDuplicate " + flag);

    flag = containsDuplicate(new int[] { 1, 2, 3, 4 });
    System.out.println("containsDuplicate " + flag);

    flag = containsDuplicate(new int[] { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 });
    System.out.println("containsDuplicate " + flag);
  }

  public static boolean containsDuplicate(int[] nums) 
  {
    HashSet<Integer> set = new HashSet<>();
    for (int i = 0; i < nums.length; i++) 
    {
      if (set.contains(nums[i]))
        return true;
      set.add(nums[i]);
    }
    return false;
  }
}

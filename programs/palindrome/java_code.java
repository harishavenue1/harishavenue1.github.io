package programs.palindrome;

public class java_code 
{
    public static boolean isPalindrome(String str) 
    {
        
        // Java: StringBuilder for efficient string manipulation
        // Chain: constructor -> .reverse() -> .toString()
        String reversed = new StringBuilder(str).reverse().toString();
        
        // Java: .equals() for string content comparison (not ==)
        return str.equals(reversed);
    }

    public static void main(String[] args) 
    {
        String str = "radar";
        if (isPalindrome(str))
            System.out.println(str + " is a palindrome.");
        else
            System.out.println(str + " is not a palindrome.");
    }
}

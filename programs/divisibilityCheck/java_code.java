public class DivisibilityCheck {
    public static void main(String[] args) {
        int num = 64;
        System.out.println("Number: " + num);
        
        // Traditional modulo approach
        if (num % 32 == 0) {
            System.out.println("abc");
        } else if (num % 16 == 0) {
            System.out.println("b");
        } else if (num % 8 == 0) {
            System.out.println("a");
        } else {
            System.out.println("none");
        }
        
        // Bitwise approach (tricky interview method)
        System.out.println("\nBitwise approach:");
        if ((num & 31) == 0) {
            System.out.println("abc");
        } else if ((num & 15) == 0) {
            System.out.println("b");
        } else if ((num & 7) == 0) {
            System.out.println("a");
        } else {
            System.out.println("none");
        }
    }
}
using System;

class DivisibilityCheck {
    static void Main() {
        int num = 64;
        Console.WriteLine("Number: " + num);
        
        // Traditional modulo approach
        if (num % 32 == 0) {
            Console.WriteLine("abc");
        } else if (num % 16 == 0) {
            Console.WriteLine("b");
        } else if (num % 8 == 0) {
            Console.WriteLine("a");
        } else {
            Console.WriteLine("none");
        }
        
        // Bitwise approach (tricky interview method)
        Console.WriteLine("\nBitwise approach:");
        if ((num & 31) == 0) {
            Console.WriteLine("abc");
        } else if ((num & 15) == 0) {
            Console.WriteLine("b");
        } else if ((num & 7) == 0) {
            Console.WriteLine("a");
        } else {
            Console.WriteLine("none");
        }
    }
}
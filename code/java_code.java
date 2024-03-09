package code;

public class java_code {
    public static void main(String[] args) {
        int n = 10; // Change the value of n for different number of Fibonacci numbers
        int a = 0, b = 1;
        System.out.println("Fibonacci Series:");
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int sum = a + b;
            a = b;
            b = sum;
        }
    }
}

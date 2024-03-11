package programs.fibonacci;

class java_code {
    public static void main(String[] args) {
        int n = 10; // Change the value of n for different number of Fibonacci numbers
        int a = 0, b = 1, sum = 0;
        System.out.println("Fibonacci Series:");
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            sum = a + b;
            a = b;
            b = sum;
        }
    }
}
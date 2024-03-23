package programs.countBits;

import java.util.*;

public class java_code {
    public static void main(String[] args) {
        int num = 2;
        int[] output = countBits(num);
        System.out.println("For Num = " + num + ", bits are " + Arrays.toString(output));

        num = 5;
        output = countBits(num);
        System.out.println("For Num = " + num + ", bits are " + Arrays.toString(output));
    }

    public static int[] countBits(int n) {
        // to return bits in each int
        int[] arr = new int[n + 1];

        int temp;
        for (int i = 1; i <= n; i++) {
            temp = i;
            while (temp != 0) {
                if (temp % 2 != 0) {
                    arr[i] += 1;
                }
                temp /= 2;
            }
        }
        return arr;
    }
}
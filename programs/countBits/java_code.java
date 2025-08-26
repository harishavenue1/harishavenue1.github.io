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
        
        // Java: Array to store count of 1-bits for each number from 0 to n
        int[] arr = new int[n + 1];

        int temp;
        
        // Java: Iterate through each number from 1 to n
        for (int i = 1; i <= n; i++) {
            temp = i;
            
            // Java: Count 1-bits by checking each bit position
            while (temp != 0) {
                
                // Java: Check if least significant bit is 1
                if (temp % 2 != 0) {
                    arr[i] += 1;  // Increment count of 1-bits
                }
                
                // Java: Right shift by dividing by 2
                temp /= 2;
            }
        }
        
        return arr;
    }
}
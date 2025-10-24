import java.util.*;

public class ReverseWordsInSentence {
    public static void main(String[] args) {
        String s = "your code goes here";
        String[] sArr = s.split(" ");
        
        // way1 - using StringBuilder
        for (int i=0; i<sArr.length; i++) {
            String str = sArr[i];
            str = new StringBuilder(str).reverse().toString();
            sArr[i] = str;
        }
        System.out.println("Final String reversed is "+ Arrays.toString(sArr));
        
        // way2 - manual reversal
        sArr = s.split(" ");
        for (int i=0; i<sArr.length; i++) {
            String str = sArr[i];
            String newStr = "";
            for (int j=str.length()-1; j>=0; j--) {
                newStr+= str.charAt(j);
            }
            sArr[i] = newStr;
        }
        System.out.println("Final String reversed is "+ Arrays.toString(sArr));
    }
}
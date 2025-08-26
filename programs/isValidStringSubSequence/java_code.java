package programs.isValidStringSubSequence;

class java_code {
    public static void main(String[] args) {

        // check if str1 chars are in str2 [subsequence]
        String str1 = "gksr%ek@@@";
        String str2 = "geeksforge%eks@@@";
        boolean isValid = isValidSubSequence(str1, str2);
        System.out.println("Valid SubSequence " + isValid);
    }

    public static boolean isValidSubSequence(String s1, String s2) {
        
        // Java: Get string lengths using .length() method
        int m = s1.length();
        int n = s2.length();

        
        // Java: Pointer for subsequence string
        int j = 0;
        
        // Java: Iterate through main string
        for (int i = 0; i < n && j < m; i++) {
            
            // Java: .charAt() to compare characters
            if (s1.charAt(j) == s2.charAt(i))
                j++;  // Move subsequence pointer forward
        }

        
        // Java: Check if all characters of subsequence were found
        return j == m;
    }
}
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
        int m = s1.length();
        int n = s2.length();

        int j = 0;
        for (int i = 0; i < n && j < m; i++) {
            if (s1.charAt(j) == s2.charAt(i))
                j++;
        }

        return j == m;
    }
}
using System;
using System.Linq;

class ReverseWordsInSentence {
    static void Main() {
        string s = "your code goes here";
        string[] sArr = s.Split(' ');
        
        // way1 - using built-in reverse
        for (int i = 0; i < sArr.Length; i++) {
            sArr[i] = new string(sArr[i].Reverse().ToArray());
        }
        Console.WriteLine("Final String reversed is [" + string.Join(", ", sArr) + "]");
        
        // way2 - manual reversal
        sArr = s.Split(' ');
        for (int i = 0; i < sArr.Length; i++) {
            string str = sArr[i];
            string newStr = "";
            for (int j = str.Length - 1; j >= 0; j--) {
                newStr += str[j];
            }
            sArr[i] = newStr;
        }
        Console.WriteLine("Final String reversed is [" + string.Join(", ", sArr) + "]");
    }
}
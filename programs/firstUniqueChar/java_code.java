import java.util.*;

public class FirstUniqueChar {
    public static void main(String[] args) {
        String s = "HarishHaresh";
        
        // way1 - count occurrences
        HashMap<Character, Integer> map = new LinkedHashMap<>();
        for (char c: s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        
        for (char k: map.keySet()) {
            if (map.get(k) == 1) {
                System.out.println("First Unique Char is -> " + k);
                break;
            }
        }
        
        // way2 - add/remove approach
        HashSet<Character> set = new LinkedHashSet<>();
        for (char c: s.toCharArray()) {
            if (set.contains(c)) {
                set.remove(c);
            } else {
                set.add(c);
            }
        }
        
        if (set.size() == 0) {
            System.out.println("There are no Unique Chars");
        } else {
            for (char c: set) {
                System.out.println("First Unique Char is -> "+ c);
                break;
            }
        }
    }
}
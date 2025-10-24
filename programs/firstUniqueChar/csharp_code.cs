using System;
using System.Collections.Generic;
using System.Linq;

class FirstUniqueChar {
    static void Main() {
        string s = "HarishHaresh";
        
        // way1 - count occurrences
        var map = new Dictionary<char, int>();
        foreach (char c in s) {
            map[c] = map.ContainsKey(c) ? map[c] + 1 : 1;
        }
        
        foreach (var k in map.Keys) {
            if (map[k] == 1) {
                Console.WriteLine("First Unique Char is -> " + k);
                break;
            }
        }
        
        // way2 - add/remove approach
        var set = new HashSet<char>();
        var order = new List<char>();
        
        foreach (char c in s) {
            if (set.Contains(c)) {
                set.Remove(c);
                order.Remove(c);
            } else {
                set.Add(c);
                order.Add(c);
            }
        }
        
        if (set.Count == 0) {
            Console.WriteLine("There are no Unique Chars");
        } else {
            Console.WriteLine("First Unique Char is -> " + order.First(c => set.Contains(c)));
        }
    }
}
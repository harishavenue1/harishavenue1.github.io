using System;
using System.Collections.Generic;
using System.Linq;

class SortByFirstOccurrence {
    static void Main() {
        int[] arr = {5,6,1,2,3,4,5,6,1,2,3};
        Console.WriteLine("Initial List [" + string.Join(", ", arr) + "]");
        
        var map = new Dictionary<int, int>();
        foreach(int i in arr) {
            map[i] = map.ContainsKey(i) ? map[i] + 1 : 1;
        }
        
        var newList = new List<int>();
        foreach(var k in map.Keys) {
            for(int v = 0; v < map[k]; v++) {
                newList.Add(k);
            }
        }
        Console.WriteLine("New List [" + string.Join(", ", newList) + "]");
    }
}
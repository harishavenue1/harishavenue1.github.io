import java.util.*;

public class SortByFirstOccurrence {
    public static void main(String[] args) {
        Integer[] arr = {5,6,1,2,3,4,5,6,1,2,3};
        List<Integer> li = Arrays.asList(arr);
        System.out.println("Initial List " + li);
        
        HashMap<Integer, Integer> map = new LinkedHashMap<>();
        for(int i: li) {
            map.put(i, map.getOrDefault(i,0)+1);
        }
        
        List<Integer> newLi = new ArrayList<>();
        for (int k: map.keySet()) {
            for (int v=0; v<map.get(k); v++) {
                newLi.add(k);
            }
        }
        System.out.println("New List " + newLi);
    }
}
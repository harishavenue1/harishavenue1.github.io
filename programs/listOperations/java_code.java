import java.util.*;

public class ListOperations {
    public static void main(String[] args) {
        // Create and initialize list
        List<String> fruits = new ArrayList<>();
        fruits.add("apple");
        fruits.add("banana");
        fruits.add("cherry");
        System.out.println("Initial list: " + fruits);
        
        // Add operations
        fruits.add(1, "orange");
        fruits.addAll(Arrays.asList("grape", "mango"));
        System.out.println("After adding: " + fruits);
        
        // Access operations
        System.out.println("First item: " + fruits.get(0));
        System.out.println("Index of banana: " + fruits.indexOf("banana"));
        System.out.println("Contains apple: " + fruits.contains("apple"));
        
        // Modify operations
        fruits.set(0, "pineapple");
        System.out.println("After replacing: " + fruits);
        
        // Remove operations
        fruits.remove("banana");
        fruits.remove(0);
        System.out.println("After removing: " + fruits);
        
        // Size and empty check
        System.out.println("Size: " + fruits.size());
        System.out.println("Is empty: " + fruits.isEmpty());
        
        // Sort and reverse
        Collections.sort(fruits);
        System.out.println("Sorted: " + fruits);
        Collections.reverse(fruits);
        System.out.println("Reversed: " + fruits);
        
        // Convert List to Array
        String[] fruitsArray = fruits.toArray(new String[0]);
        System.out.println("List to Array: " + Arrays.toString(fruitsArray));
        
        // Convert Array to List
        String[] newArray = {"kiwi", "peach", "plum"};
        List<String> newList = Arrays.asList(newArray);
        System.out.println("Array to List: " + newList);
        
        // Clear list
        fruits.clear();
        System.out.println("After clear: " + fruits);
    }
}
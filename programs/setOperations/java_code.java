import java.util.*;

public class SetOperations {
    public static void main(String[] args) {
        // Create and initialize sets
        Set<String> fruits = new HashSet<>();
        fruits.add("apple");
        fruits.add("banana");
        fruits.add("cherry");
        fruits.add("apple"); // Duplicate - won't be added
        System.out.println("Initial set: " + fruits);
        
        // Add operations
        fruits.addAll(Arrays.asList("grape", "mango", "banana"));
        System.out.println("After adding: " + fruits);
        
        // Check operations
        System.out.println("Contains apple: " + fruits.contains("apple"));
        System.out.println("Size: " + fruits.size());
        System.out.println("Is empty: " + fruits.isEmpty());
        
        // Create second set for operations
        Set<String> citrus = new HashSet<>(Arrays.asList("orange", "lemon", "grape"));
        System.out.println("Citrus set: " + citrus);
        
        // Set operations - Union
        Set<String> union = new HashSet<>(fruits);
        union.addAll(citrus);
        System.out.println("Union: " + union);
        
        // Set operations - Intersection
        Set<String> intersection = new HashSet<>(fruits);
        intersection.retainAll(citrus);
        System.out.println("Intersection: " + intersection);
        
        // Set operations - Difference
        Set<String> difference = new HashSet<>(fruits);
        difference.removeAll(citrus);
        System.out.println("Difference (fruits - citrus): " + difference);
        
        // Check subset/superset
        Set<String> subset = new HashSet<>(Arrays.asList("apple", "banana"));
        System.out.println("Is subset contained: " + fruits.containsAll(subset));
        
        // Convert to array and list
        String[] fruitsArray = fruits.toArray(new String[0]);
        System.out.println("Set to Array: " + Arrays.toString(fruitsArray));
        
        List<String> fruitsList = new ArrayList<>(fruits);
        System.out.println("Set to List: " + fruitsList);
        
        // Iterate through set
        System.out.print("Iteration: ");
        for (String fruit : fruits) {
            System.out.print(fruit + " ");
        }
        System.out.println();
        
        // Remove operations
        fruits.remove("banana");
        System.out.println("After removing banana: " + fruits);
        
        // Clear set
        fruits.clear();
        System.out.println("After clear: " + fruits);
    }
}
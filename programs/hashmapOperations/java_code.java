import java.util.*;

public class HashmapOperations {
    public static void main(String[] args) {
        // Create and initialize HashMap
        Map<String, Integer> fruits = new HashMap<>();
        fruits.put("apple", 5);
        fruits.put("banana", 3);
        fruits.put("cherry", 8);
        System.out.println("Initial map: " + fruits);
        
        // Put operations
        fruits.put("apple", 10); // Update existing
        fruits.putIfAbsent("grape", 6); // Add if not exists
        fruits.putAll(Map.of("mango", 4, "orange", 7));
        System.out.println("After putting: " + fruits);
        
        // Get operations
        System.out.println("Apple count: " + fruits.get("apple"));
        System.out.println("Kiwi count: " + fruits.getOrDefault("kiwi", 0));
        
        // Check operations
        System.out.println("Contains apple: " + fruits.containsKey("apple"));
        System.out.println("Contains value 8: " + fruits.containsValue(8));
        System.out.println("Size: " + fruits.size());
        System.out.println("Is empty: " + fruits.isEmpty());
        
        // Compute operations
        fruits.compute("apple", (k, v) -> v + 2);
        fruits.computeIfAbsent("pear", k -> 1);
        fruits.computeIfPresent("banana", (k, v) -> v * 2);
        System.out.println("After compute operations: " + fruits);
        
        // Merge operation
        fruits.merge("apple", 5, Integer::sum);
        System.out.println("After merge: " + fruits);
        
        // Replace operations
        fruits.replace("cherry", 15);
        fruits.replace("banana", 6, 12); // Replace only if current value is 6
        fruits.replaceAll((k, v) -> v > 10 ? v : v + 1);
        System.out.println("After replace operations: " + fruits);
        
        // Iteration methods
        System.out.println("Keys: " + fruits.keySet());
        System.out.println("Values: " + fruits.values());
        System.out.println("Entries: " + fruits.entrySet());
        
        // Iterate through entries
        System.out.println("Iteration:");
        for (Map.Entry<String, Integer> entry : fruits.entrySet()) {
            System.out.println("  " + entry.getKey() + " = " + entry.getValue());
        }
        
        // forEach with lambda
        System.out.println("forEach iteration:");
        fruits.forEach((k, v) -> System.out.println("  " + k + " -> " + v));
        
        // Create second map for operations
        Map<String, Integer> citrus = new HashMap<>();
        citrus.put("orange", 12);
        citrus.put("lemon", 3);
        citrus.put("lime", 5);
        
        // Clone and merge maps
        Map<String, Integer> combined = new HashMap<>(fruits);
        citrus.forEach((k, v) -> combined.merge(k, v, Integer::sum));
        System.out.println("Combined maps: " + combined);
        
        // Remove operations
        fruits.remove("banana");
        fruits.remove("apple", 17); // Remove only if value matches
        System.out.println("After removing: " + fruits);
        
        // Clear map
        fruits.clear();
        System.out.println("After clear: " + fruits);
    }
}
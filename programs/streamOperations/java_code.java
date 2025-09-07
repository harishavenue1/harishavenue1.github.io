import java.util.*;
import java.util.stream.*;

public class java_code {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date", "elderberry");
        
        System.out.println("Original numbers: " + numbers);
        System.out.println("Original words: " + words);
        
        // Filter operations
        List<Integer> evenNumbers = numbers.stream()
            .filter(n -> n % 2 == 0)
            .collect(Collectors.toList());
        System.out.println("Even numbers: " + evenNumbers);
        
        // Map operations
        List<Integer> squared = numbers.stream()
            .map(n -> n * n)
            .collect(Collectors.toList());
        System.out.println("Squared numbers: " + squared);
        
        List<String> upperWords = words.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        System.out.println("Uppercase words: " + upperWords);
        
        // FlatMap operations
        List<List<Integer>> nestedList = Arrays.asList(
            Arrays.asList(1, 2), Arrays.asList(3, 4), Arrays.asList(5, 6)
        );
        List<Integer> flattened = nestedList.stream()
            .flatMap(Collection::stream)
            .collect(Collectors.toList());
        System.out.println("Flattened: " + flattened);
        
        // Reduce operations
        int sum = numbers.stream().reduce(0, Integer::sum);
        System.out.println("Sum: " + sum);
        
        Optional<Integer> max = numbers.stream().reduce(Integer::max);
        System.out.println("Max: " + max.orElse(0));
        
        // Collect operations
        Set<Integer> numberSet = numbers.stream().collect(Collectors.toSet());
        System.out.println("As Set: " + numberSet);
        
        String joined = words.stream().collect(Collectors.joining(", "));
        System.out.println("Joined: " + joined);
        
        // Grouping
        Map<Integer, List<String>> groupedByLength = words.stream()
            .collect(Collectors.groupingBy(String::length));
        System.out.println("Grouped by length: " + groupedByLength);
        
        // Partitioning
        Map<Boolean, List<Integer>> partitioned = numbers.stream()
            .collect(Collectors.partitioningBy(n -> n > 5));
        System.out.println("Partitioned (>5): " + partitioned);
        
        // Sorting
        List<String> sorted = words.stream()
            .sorted()
            .collect(Collectors.toList());
        System.out.println("Sorted words: " + sorted);
        
        List<String> sortedByLength = words.stream()
            .sorted(Comparator.comparing(String::length))
            .collect(Collectors.toList());
        System.out.println("Sorted by length: " + sortedByLength);
        
        // Distinct
        List<Integer> duplicates = Arrays.asList(1, 2, 2, 3, 3, 4, 5);
        List<Integer> unique = duplicates.stream()
            .distinct()
            .collect(Collectors.toList());
        System.out.println("Unique: " + unique);
        
        // Limit and Skip
        List<Integer> limited = numbers.stream()
            .limit(5)
            .collect(Collectors.toList());
        System.out.println("Limited (5): " + limited);
        
        List<Integer> skipped = numbers.stream()
            .skip(5)
            .collect(Collectors.toList());
        System.out.println("Skipped (5): " + skipped);
        
        // Terminal operations
        long count = numbers.stream().filter(n -> n > 5).count();
        System.out.println("Count > 5: " + count);
        
        boolean anyMatch = numbers.stream().anyMatch(n -> n > 8);
        System.out.println("Any > 8: " + anyMatch);
        
        boolean allMatch = numbers.stream().allMatch(n -> n > 0);
        System.out.println("All > 0: " + allMatch);
        
        Optional<Integer> first = numbers.stream().filter(n -> n > 5).findFirst();
        System.out.println("First > 5: " + first.orElse(-1));
        
        // Parallel streams
        int parallelSum = numbers.parallelStream()
            .mapToInt(Integer::intValue)
            .sum();
        System.out.println("Parallel sum: " + parallelSum);
    }
}
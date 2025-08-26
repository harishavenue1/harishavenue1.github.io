import java.util.*;
import java.util.stream.Collectors;

class Person {
    String name;
    int age;
    int score;
    
    Person(String name, int age, int score) {
        this.name = name;
        this.age = age;
        this.score = score;
    }
    
    @Override
    public String toString() {
        return String.format("{name='%s', age=%d, score=%d}", name, age, score);
    }
}

class Task {
    String name;
    String priority;
    int timestamp;
    
    Task(String name, String priority, int timestamp) {
        this.name = name;
        this.priority = priority;
        this.timestamp = timestamp;
    }
    
    @Override
    public String toString() {
        return String.format("{name='%s', priority='%s', timestamp=%d}", name, priority, timestamp);
    }
}

public class ComparatorLogic {
    
    // Java: Custom string comparator - length first, then alphabetical
    public static class CustomStringComparator implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            
            // Compare by length first
            if (a.length() != b.length()) {
                return Integer.compare(a.length(), b.length());
            }
            
            
            // Java: Alphabetical comparison if lengths are equal
            return a.compareTo(b);
        }
    }
    
    // Java: Multi-criteria person comparator
    public static class PersonComparator implements Comparator<Person> {
        @Override
        public int compare(Person p1, Person p2) {
            
            // Compare by age first
            int ageComparison = Integer.compare(p1.age, p2.age);
            if (ageComparison != 0) {
                return ageComparison;
            }
            
            
            // Compare by name if ages are equal
            int nameComparison = p1.name.compareTo(p2.name);
            if (nameComparison != 0) {
                return nameComparison;
            }
            
            
            // Java: Compare by score (descending) if names are equal
            return Integer.compare(p2.score, p1.score);
        }
    }
    
    // Java: Priority-based task comparator
    public static class TaskComparator implements Comparator<Task> {
        private final Map<String, Integer> priorityOrder = Map.of(
            "high", 3,
            "medium", 2,
            "low", 1
        );
        
        @Override
        public int compare(Task t1, Task t2) {
            
            // Compare by priority first (higher priority first)
            int p1 = priorityOrder.getOrDefault(t1.priority, 1);
            int p2 = priorityOrder.getOrDefault(t2.priority, 1);
            
            if (p1 != p2) {
                return Integer.compare(p2, p1);
            }
            
            
            // Java: Compare by timestamp if priorities are equal
            return Integer.compare(t1.timestamp, t2.timestamp);
        }
    }
    
    public static List<String> sortStringsCustom(List<String> strings) {
        
        // Java: Sort using custom comparator
        return strings.stream()
                .sorted(new CustomStringComparator())
                .collect(Collectors.toList());
    }
    
    public static List<Person> sortPeopleMultiCriteria(List<Person> people) {
        
        // Java: Sort using multi-criteria comparator
        return people.stream()
                .sorted(new PersonComparator())
                .collect(Collectors.toList());
    }
    
    public static <T> T findKthElement(List<T> list, int k, Comparator<T> comparator) {
        
        // Java: Sort with custom comparator and return kth element
        List<T> sorted = list.stream()
                .sorted(comparator)
                .collect(Collectors.toList());
        
        if (k >= 1 && k <= sorted.size()) {
            return sorted.get(k - 1);
        }
        return null;
    }
    
    public static <T> List<T> mergeSortedArrays(List<T> arr1, List<T> arr2, Comparator<T> comparator) {
        
        // Java: Merge two sorted arrays using comparator
        List<T> result = new ArrayList<>();
        int i = 0, j = 0;
        
        while (i < arr1.size() && j < arr2.size()) {
            if (comparator.compare(arr1.get(i), arr2.get(j)) <= 0) {
                result.add(arr1.get(i));
                i++;
            } else {
                result.add(arr2.get(j));
                j++;
            }
        }
        
        
        // Java: Add remaining elements
        while (i < arr1.size()) {
            result.add(arr1.get(i));
            i++;
        }
        
        while (j < arr2.size()) {
            result.add(arr2.get(j));
            j++;
        }
        
        return result;
    }
    
    public static <T> int binarySearchWithComparator(List<T> arr, T target, Comparator<T> comparator) {
        
        // Java: Binary search with custom comparator
        int left = 0, right = arr.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int comparison = comparator.compare(arr.get(mid), target);
            
            if (comparison == 0) {
                return mid;
            } else if (comparison < 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
    
    public static void main(String[] args) {
        
        // Test string sorting with custom comparator
        List<String> strings = Arrays.asList("apple", "pie", "a", "longer", "cat");
        List<String> sortedStrings = sortStringsCustom(strings);
        System.out.println("Custom sorted strings: " + sortedStrings);
        
        
        // Test multi-criteria person sorting
        List<Person> people = Arrays.asList(
            new Person("Alice", 30, 85),
            new Person("Bob", 25, 90),
            new Person("Charlie", 25, 95),
            new Person("Alice", 30, 80)
        );
        
        List<Person> sortedPeople = sortPeopleMultiCriteria(people);
        System.out.println("\nSorted people:");
        sortedPeople.forEach(person -> System.out.println("  " + person));
        
        
        // Test priority-based task sorting
        List<Task> tasks = Arrays.asList(
            new Task("Task1", "low", 100),
            new Task("Task2", "high", 50),
            new Task("Task3", "medium", 75),
            new Task("Task4", "high", 25)
        );
        
        List<Task> sortedTasks = tasks.stream()
                .sorted(new TaskComparator())
                .collect(Collectors.toList());
        
        System.out.println("\nSorted tasks by priority:");
        sortedTasks.forEach(task -> System.out.println("  " + task));
        
        
        // Test kth element finding
        List<Integer> numbers = Arrays.asList(64, 34, 25, 12, 22, 11, 90);
        Integer kthElement = findKthElement(numbers, 3, Integer::compareTo);
        System.out.println("\n3rd smallest element: " + kthElement);
        
        
        // Test merging sorted arrays
        List<Integer> arr1 = Arrays.asList(1, 3, 5, 7);
        List<Integer> arr2 = Arrays.asList(2, 4, 6, 8);
        List<Integer> merged = mergeSortedArrays(arr1, arr2, Integer::compareTo);
        System.out.println("\nMerged arrays: " + merged);
    }
}
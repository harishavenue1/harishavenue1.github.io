from functools import cmp_to_key

def custom_comparator(a, b):
    """Custom comparator function for complex sorting logic"""
    
    # Python: Compare by length first, then alphabetically
    if len(a) != len(b):
        return len(a) - len(b)
    
    # Python: Alphabetical comparison if lengths are equal
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def sort_with_multiple_criteria(data):
    """Sort data using multiple comparison criteria"""
    
    # Python: Lambda function for multi-criteria sorting
    # Sort by: 1) Age (ascending), 2) Name (alphabetical), 3) Score (descending)
    return sorted(data, key=lambda x: (x['age'], x['name'], -x['score']))

def compare_objects(obj1, obj2):
    """Compare two objects with custom logic"""
    
    # Python: Priority-based comparison
    priority_order = {'high': 3, 'medium': 2, 'low': 1}
    
    # Compare by priority first
    p1 = priority_order.get(obj1.get('priority', 'low'), 1)
    p2 = priority_order.get(obj2.get('priority', 'low'), 1)
    
    if p1 != p2:
        return p2 - p1  # Higher priority first
    
    
    # Python: Compare by timestamp if priorities are equal
    return obj1.get('timestamp', 0) - obj2.get('timestamp', 0)

def sort_strings_custom(strings):
    """Sort strings using custom comparator"""
    
    # Python: Using cmp_to_key to convert comparator function
    return sorted(strings, key=cmp_to_key(custom_comparator))

def find_kth_element(arr, k, comparator=None):
    """Find kth smallest element using custom comparator"""
    
    # Python: Sort with custom comparator if provided
    if comparator:
        sorted_arr = sorted(arr, key=cmp_to_key(comparator))
    else:
        sorted_arr = sorted(arr)
    
    
    # Python: Return kth element (1-indexed)
    if 1 <= k <= len(sorted_arr):
        return sorted_arr[k-1]
    return None

def merge_sorted_arrays(arr1, arr2, comparator=None):
    """Merge two sorted arrays using custom comparator"""
    
    # Python: Initialize pointers and result array
    i, j = 0, 0
    result = []
    
    
    # Python: Merge arrays using comparator logic
    while i < len(arr1) and j < len(arr2):
        if comparator:
            comparison = comparator(arr1[i], arr2[j])
        else:
            comparison = -1 if arr1[i] < arr2[j] else (1 if arr1[i] > arr2[j] else 0)
        
        if comparison <= 0:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    
    # Python: Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

def binary_search_with_comparator(arr, target, comparator):
    """Binary search using custom comparator"""
    
    # Python: Binary search with custom comparison logic
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        comparison = comparator(arr[mid], target)
        
        if comparison == 0:
            return mid
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test the comparator logic
if __name__ == "__main__":
    
    # Test string sorting with custom comparator
    strings = ["apple", "pie", "a", "longer", "cat"]
    sorted_strings = sort_strings_custom(strings)
    print(f"Custom sorted strings: {sorted_strings}")
    
    
    # Test multi-criteria object sorting
    people = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 90},
        {'name': 'Charlie', 'age': 25, 'score': 95},
        {'name': 'Alice', 'age': 30, 'score': 80}
    ]
    
    sorted_people = sort_with_multiple_criteria(people)
    print(f"\nSorted people:")
    for person in sorted_people:
        print(f"  {person}")
    
    
    # Test priority-based object comparison
    tasks = [
        {'name': 'Task1', 'priority': 'low', 'timestamp': 100},
        {'name': 'Task2', 'priority': 'high', 'timestamp': 50},
        {'name': 'Task3', 'priority': 'medium', 'timestamp': 75},
        {'name': 'Task4', 'priority': 'high', 'timestamp': 25}
    ]
    
    sorted_tasks = sorted(tasks, key=cmp_to_key(compare_objects))
    print(f"\nSorted tasks by priority:")
    for task in sorted_tasks:
        print(f"  {task}")
    
    
    # Test kth element finding
    numbers = [64, 34, 25, 12, 22, 11, 90]
    kth_element = find_kth_element(numbers, 3)
    print(f"\n3rd smallest element: {kth_element}")
    
    
    # Test merging sorted arrays
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    merged = merge_sorted_arrays(arr1, arr2)
    print(f"\nMerged arrays: {merged}")
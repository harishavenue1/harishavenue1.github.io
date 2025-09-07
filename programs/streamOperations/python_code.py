# Python functional programming (equivalent to streams)
from functools import reduce
from itertools import groupby, chain
from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original numbers:", numbers)
print("Original words:", words)

# Filter operations
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# List comprehension (Pythonic way)
even_numbers_comp = [n for n in numbers if n % 2 == 0]
print("Even numbers (comprehension):", even_numbers_comp)

# Map operations
squared = list(map(lambda n: n * n, numbers))
print("Squared numbers:", squared)

# List comprehension for mapping
squared_comp = [n * n for n in numbers]
print("Squared (comprehension):", squared_comp)

upper_words = list(map(str.upper, words))
print("Uppercase words:", upper_words)

# FlatMap equivalent (using itertools.chain)
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = list(chain.from_iterable(nested_list))
print("Flattened:", flattened)

# List comprehension for flattening
flattened_comp = [item for sublist in nested_list for item in sublist]
print("Flattened (comprehension):", flattened_comp)

# Reduce operations
sum_result = reduce(lambda a, b: a + b, numbers)
print("Sum:", sum_result)

# Built-in functions (more Pythonic)
sum_builtin = sum(numbers)
max_builtin = max(numbers)
min_builtin = min(numbers)
print(f"Sum (builtin): {sum_builtin}, Max: {max_builtin}, Min: {min_builtin}")

# Any and All operations
has_even = any(n % 2 == 0 for n in numbers)
print("Has even:", has_even)

all_positive = all(n > 0 for n in numbers)
print("All positive:", all_positive)

# Find operations (using next with generator)
first_even = next((n for n in numbers if n % 2 == 0), None)
print("First even:", first_even)

# Sorting
sorted_words = sorted(words)
print("Sorted words:", sorted_words)

sorted_by_length = sorted(words, key=len)
print("Sorted by length:", sorted_by_length)

# Reverse
reversed_numbers = list(reversed(numbers))
print("Reversed:", reversed_numbers)

# Slicing (equivalent to limit/skip)
limited = numbers[:5]
print("Limited (5):", limited)

skipped = numbers[5:]
print("Skipped (5):", skipped)

# Unique values (using set)
duplicates = [1, 2, 2, 3, 3, 4, 5]
unique = list(set(duplicates))
print("Unique:", unique)

# Maintain order while removing duplicates
unique_ordered = list(dict.fromkeys(duplicates))
print("Unique (ordered):", unique_ordered)

# Group by
words_by_length = {}
for word in words:
    length = len(word)
    if length not in words_by_length:
        words_by_length[length] = []
    words_by_length[length].append(word)
print("Grouped by length:", words_by_length)

# Using itertools.groupby (requires sorted input)
sorted_words_by_len = sorted(words, key=len)
grouped = {k: list(g) for k, g in groupby(sorted_words_by_len, key=len)}
print("Grouped by length (itertools):", grouped)

# Dictionary comprehension for grouping
grouped_comp = {}
for word in words:
    grouped_comp.setdefault(len(word), []).append(word)
print("Grouped (dict comprehension):", grouped_comp)

# Partition
greater_than_5 = [n for n in numbers if n > 5]
less_equal_5 = [n for n in numbers if n <= 5]
print(f"Partitioned (>5): Greater={greater_than_5}, LessEqual={less_equal_5}")

# Join
joined = ", ".join(words)
print("Joined:", joined)

# Enumerate (with index)
print("Enumerated:")
for i, word in enumerate(words):
    print(f"  {i}: {word}")

# Zip operations
zipped = list(zip(numbers[:3], words[:3]))
print("Zipped:", zipped)

zipped_strings = [f"{n}-{w}" for n, w in zip(numbers[:3], words[:3])]
print("Zipped strings:", zipped_strings)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

# Counter for frequency
char_count = Counter("hello world")
print("Character count:", char_count)
print("Most common:", char_count.most_common(3))

# Complex chaining
complex_result = [
    n * 2 for n in numbers 
    if n > 3 and n < 8
]
print("Complex operation:", complex_result)

# Generator expressions (memory efficient)
squared_gen = (n * n for n in numbers)
print("Squared (generator):", list(squared_gen))

# Filter and map combined
filtered_mapped = [n * 2 for n in numbers if n % 2 == 0]
print("Filtered and mapped:", filtered_mapped)

# Chunk list
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

chunked = chunk_list(numbers, 3)
print("Chunked (3):", chunked)

# Count occurrences
count_2 = [1, 2, 2, 3, 2].count(2)
print("Count of 2:", count_2)
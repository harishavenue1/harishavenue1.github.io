# Create and initialize sets
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")  # Duplicate - won't be added
print("Initial set:", fruits)

# Add operations
fruits.update(["grape", "mango", "banana"])
print("After adding:", fruits)

# Check operations
print("Contains apple:", "apple" in fruits)
print("Length:", len(fruits))
print("Is empty:", len(fruits) == 0)

# Create second set for operations
citrus = {"orange", "lemon", "grape"}
print("Citrus set:", citrus)

# Set operations - Union
union = fruits | citrus  # or fruits.union(citrus)
print("Union:", union)

# Set operations - Intersection
intersection = fruits & citrus  # or fruits.intersection(citrus)
print("Intersection:", intersection)

# Set operations - Difference
difference = fruits - citrus  # or fruits.difference(citrus)
print("Difference (fruits - citrus):", difference)

# Set operations - Symmetric Difference
sym_diff = fruits ^ citrus  # or fruits.symmetric_difference(citrus)
print("Symmetric Difference:", sym_diff)

# Check subset/superset
subset = {"apple", "banana"}
print("Is subset:", subset.issubset(fruits))
print("Is superset:", fruits.issuperset(subset))
print("Is disjoint:", fruits.isdisjoint(citrus))

# Convert to list and tuple
fruits_list = list(fruits)
print("Set to List:", fruits_list)

fruits_tuple = tuple(fruits)
print("Set to Tuple:", fruits_tuple)

# Set comprehension
vowel_fruits = {fruit for fruit in fruits if fruit[0] in 'aeiou'}
print("Fruits starting with vowels:", vowel_fruits)

# Copy operations
fruits_copy = fruits.copy()
print("Set copy:", fruits_copy)

# Frozen set (immutable set)
frozen_fruits = frozenset(fruits)
print("Frozen set:", frozen_fruits)

# In-place operations
fruits_copy.intersection_update(citrus)
print("After intersection_update:", fruits_copy)

fruits_copy = fruits.copy()
fruits_copy.difference_update(citrus)
print("After difference_update:", fruits_copy)

# Remove operations
fruits.remove("banana")  # Raises KeyError if not found
print("After removing banana:", fruits)

fruits.discard("nonexistent")  # No error if not found
print("After discarding nonexistent:", fruits)

# Pop random element
if fruits:
    popped = fruits.pop()
    print(f"Popped element: {popped}")
    print("After pop:", fruits)

# Clear set
fruits.clear()
print("After clear:", fruits)
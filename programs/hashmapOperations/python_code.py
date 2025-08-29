# Create and initialize dictionary
fruits = {"apple": 5, "banana": 3, "cherry": 8}
print("Initial dict:", fruits)

# Update operations
fruits["apple"] = 10  # Update existing
fruits["grape"] = 6   # Add new
fruits.update({"mango": 4, "orange": 7})
print("After updating:", fruits)

# Get operations
print("Apple count:", fruits["apple"])
print("Kiwi count:", fruits.get("kiwi", 0))

# Check operations
print("Contains apple:", "apple" in fruits)
print("Length:", len(fruits))
print("Is empty:", len(fruits) == 0)

# Dictionary methods
print("Keys:", list(fruits.keys()))
print("Values:", list(fruits.values()))
print("Items:", list(fruits.items()))

# Iteration methods
print("Iteration over keys:")
for key in fruits:
    print(f"  {key} = {fruits[key]}")

print("Iteration over items:")
for key, value in fruits.items():
    print(f"  {key} -> {value}")

# Dictionary comprehension
high_value_fruits = {k: v for k, v in fruits.items() if v > 5}
print("High value fruits:", high_value_fruits)

# Transform values
doubled_fruits = {k: v * 2 for k, v in fruits.items()}
print("Doubled values:", doubled_fruits)

# setdefault method
fruits.setdefault("pear", 2)  # Add if not exists
fruits.setdefault("apple", 99)  # Won't change existing
print("After setdefault:", fruits)

# pop operations
banana_count = fruits.pop("banana", 0)  # Remove and return value
print(f"Popped banana: {banana_count}")
print("After pop:", fruits)

# popitem (removes arbitrary item)
if fruits:
    key, value = fruits.popitem()
    print(f"Popped item: {key} = {value}")
    print("After popitem:", fruits)

# Create second dictionary
citrus = {"orange": 12, "lemon": 3, "lime": 5}
print("Citrus dict:", citrus)

# Merge dictionaries (Python 3.9+)
# combined = fruits | citrus
# For older Python versions:
combined = {**fruits, **citrus}
print("Combined dicts:", combined)

# Update with another dict
fruits_copy = fruits.copy()
fruits_copy.update(citrus)
print("Updated copy:", fruits_copy)

# Dictionary from keys
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("Dict from keys:", new_dict)

# zip to create dictionary
keys = ["x", "y", "z"]
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print("Zipped dict:", zipped_dict)

# Check for key existence
print("Has 'apple' key:", "apple" in fruits)
print("Has 'kiwi' key:", "kiwi" in fruits)

# Get all keys/values as views
keys_view = fruits.keys()
values_view = fruits.values()
print("Keys view:", keys_view)
print("Values view:", values_view)

# Clear dictionary
fruits.clear()
print("After clear:", fruits)

# defaultdict example
from collections import defaultdict

# Default dict with int (default value 0)
dd_int = defaultdict(int)
dd_int["apple"] += 1
dd_int["banana"] += 2
print("DefaultDict (int):", dict(dd_int))

# Default dict with list
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
dd_list["colors"].append("red")
print("DefaultDict (list):", dict(dd_list))

# Counter example
from collections import Counter

text = "hello world"
char_count = Counter(text)
print("Character count:", char_count)
print("Most common:", char_count.most_common(3))
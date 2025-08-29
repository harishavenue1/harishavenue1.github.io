# Create and initialize list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Add operations
fruits.insert(1, "orange")
fruits.extend(["grape", "mango"])
fruits.append("watermelon")
print("After adding:", fruits)

# Access operations
print("First item:", fruits[0])
print("Index of banana:", fruits.index("banana"))
print("Contains apple:", "apple" in fruits)

# Modify operations
fruits[0] = "pineapple"
print("After replacing:", fruits)

# Remove operations
fruits.remove("banana")
fruits.pop(0)  # Remove first element
print("After removing:", fruits)

# Size and empty check
print("Length:", len(fruits))
print("Is empty:", len(fruits) == 0)

# Sort and reverse
fruits.sort()
print("Sorted:", fruits)
fruits.reverse()
print("Reversed:", fruits)

# List comprehension and methods
print("Count of 'grape':", fruits.count("grape"))
print("Max item:", max(fruits))
print("Min item:", min(fruits))

# Convert List to Array (using array module)
import array
# For demonstration, convert to tuple (immutable sequence)
fruits_tuple = tuple(fruits)
print("List to Tuple:", fruits_tuple)

# Convert Array/Tuple to List
new_array = ("kiwi", "peach", "plum")
new_list = list(new_array)
print("Tuple to List:", new_list)

# Additional list operations
fruits_copy = fruits.copy()
print("List copy:", fruits_copy)
print("Join with comma:", ", ".join(fruits))
print("Slice [1:3]:", fruits[1:3])

# Clear list
fruits.clear()
print("After clear:", fruits)
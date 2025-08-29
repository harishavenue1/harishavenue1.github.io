// Create and initialize array (JavaScript's list equivalent)
let fruits = ["apple", "banana", "cherry"];
console.log("Initial array:", fruits);

// Add operations
fruits.splice(1, 0, "orange");
fruits.push(...["grape", "mango"]);
console.log("After adding:", fruits);

// Access operations
console.log("First item:", fruits[0]);
console.log("Index of banana:", fruits.indexOf("banana"));
console.log("Contains apple:", fruits.includes("apple"));

// Modify operations
fruits[0] = "pineapple";
console.log("After replacing:", fruits);

// Remove operations
let bananaIndex = fruits.indexOf("banana");
if (bananaIndex > -1) fruits.splice(bananaIndex, 1);
fruits.shift(); // Remove first element
console.log("After removing:", fruits);

// Size and empty check
console.log("Length:", fruits.length);
console.log("Is empty:", fruits.length === 0);

// Sort and reverse
fruits.sort();
console.log("Sorted:", fruits);
fruits.reverse();
console.log("Reversed:", fruits);

// Convert Array to different format (spread operator)
let fruitsArray = [...fruits];
console.log("Array copy:", fruitsArray);

// Convert from Array (already an array in JS)
let newArray = ["kiwi", "peach", "plum"];
let newList = Array.from(newArray);
console.log("Array to List:", newList);

// Additional array methods
console.log("Join with comma:", fruits.join(", "));
console.log("Slice (1-3):", fruits.slice(1, 3));
console.log("Filter (contains 'a'):", fruits.filter(f => f.includes('a')));
console.log("Map to uppercase:", fruits.map(f => f.toUpperCase()));

// Clear array
fruits.length = 0;
console.log("After clear:", fruits);
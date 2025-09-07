// Array methods (JavaScript's equivalent to streams)
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const words = ["apple", "banana", "cherry", "date", "elderberry"];

console.log("Original numbers:", numbers);
console.log("Original words:", words);

// Filter operations
const evenNumbers = numbers.filter(n => n % 2 === 0);
console.log("Even numbers:", evenNumbers);

// Map operations
const squared = numbers.map(n => n * n);
console.log("Squared numbers:", squared);

const upperWords = words.map(w => w.toUpperCase());
console.log("Uppercase words:", upperWords);

// FlatMap operations
const nestedArray = [[1, 2], [3, 4], [5, 6]];
const flattened = nestedArray.flatMap(arr => arr);
console.log("Flattened:", flattened);

// Reduce operations
const sum = numbers.reduce((acc, n) => acc + n, 0);
console.log("Sum:", sum);

const max = numbers.reduce((acc, n) => Math.max(acc, n));
console.log("Max:", max);

// Find operations
const firstEven = numbers.find(n => n % 2 === 0);
console.log("First even:", firstEven);

const evenIndex = numbers.findIndex(n => n % 2 === 0);
console.log("First even index:", evenIndex);

// Some and Every (equivalent to anyMatch/allMatch)
const hasEven = numbers.some(n => n % 2 === 0);
console.log("Has even:", hasEven);

const allPositive = numbers.every(n => n > 0);
console.log("All positive:", allPositive);

// Includes (contains)
const hasNumber5 = numbers.includes(5);
console.log("Has number 5:", hasNumber5);

// Sort operations
const sortedWords = [...words].sort();
console.log("Sorted words:", sortedWords);

const sortedByLength = [...words].sort((a, b) => a.length - b.length);
console.log("Sorted by length:", sortedByLength);

const sortedNumbers = [...numbers].sort((a, b) => b - a); // Descending
console.log("Sorted numbers (desc):", sortedNumbers);

// Slice (equivalent to limit/skip)
const limited = numbers.slice(0, 5);
console.log("Limited (5):", limited);

const skipped = numbers.slice(5);
console.log("Skipped (5):", skipped);

// Unique values (using Set)
const duplicates = [1, 2, 2, 3, 3, 4, 5];
const unique = [...new Set(duplicates)];
console.log("Unique:", unique);

// Group by (manual implementation)
const groupByLength = words.reduce((groups, word) => {
    const length = word.length;
    if (!groups[length]) groups[length] = [];
    groups[length].push(word);
    return groups;
}, {});
console.log("Grouped by length:", groupByLength);

// Partition (manual implementation)
const partitioned = numbers.reduce((result, n) => {
    if (n > 5) {
        result.greater.push(n);
    } else {
        result.lesser.push(n);
    }
    return result;
}, { greater: [], lesser: [] });
console.log("Partitioned (>5):", partitioned);

// Join (equivalent to collect joining)
const joined = words.join(", ");
console.log("Joined:", joined);

// Chain multiple operations
const complexOperation = numbers
    .filter(n => n > 3)
    .map(n => n * 2)
    .filter(n => n < 20)
    .sort((a, b) => b - a);
console.log("Complex operation:", complexOperation);

// ForEach (side effects)
console.log("ForEach iteration:");
numbers.forEach((n, index) => {
    if (n % 2 === 0) console.log(`  Index ${index}: ${n}`);
});

// Array.from with mapping
const fromRange = Array.from({length: 5}, (_, i) => i * 2);
console.log("Array.from range:", fromRange);

// Set operations (using Set)
const set1 = new Set([1, 2, 3, 4, 5]);
const set2 = new Set([4, 5, 6, 7, 8]);

const union = new Set([...set1, ...set2]);
console.log("Union:", Array.from(union));

const intersection = new Set([...set1].filter(x => set2.has(x)));
console.log("Intersection:", Array.from(intersection));

const difference = new Set([...set1].filter(x => !set2.has(x)));
console.log("Difference:", Array.from(difference));

// Advanced array methods
const reversed = [...numbers].reverse();
console.log("Reversed:", reversed);

// Zip (manual implementation)
const zipped = numbers.slice(0, 3).map((n, i) => `${n}-${words[i]}`);
console.log("Zipped:", zipped);

// Chunk array (manual implementation)
const chunk = (arr, size) => {
    return Array.from({length: Math.ceil(arr.length / size)}, (_, i) =>
        arr.slice(i * size, i * size + size)
    );
};
const chunked = chunk(numbers, 3);
console.log("Chunked (3):", chunked);

// Count occurrences
const countOccurrences = (arr, value) => arr.filter(x => x === value).length;
console.log("Count of 2:", countOccurrences([1, 2, 2, 3, 2], 2));
// JavaScript: Custom string comparator - length first, then alphabetical
function customStringComparator(a, b) {
    
    // Compare by length first
    if (a.length !== b.length) {
        return a.length - b.length;
    }
    
    
    // JavaScript: Alphabetical comparison if lengths are equal
    return a.localeCompare(b);
}

// JavaScript: Multi-criteria person comparator
function personComparator(p1, p2) {
    
    // Compare by age first
    if (p1.age !== p2.age) {
        return p1.age - p2.age;
    }
    
    
    // Compare by name if ages are equal
    if (p1.name !== p2.name) {
        return p1.name.localeCompare(p2.name);
    }
    
    
    // JavaScript: Compare by score (descending) if names are equal
    return p2.score - p1.score;
}

// JavaScript: Priority-based task comparator
function taskComparator(t1, t2) {
    
    // JavaScript: Priority mapping object
    const priorityOrder = { 'high': 3, 'medium': 2, 'low': 1 };
    
    const p1 = priorityOrder[t1.priority] || 1;
    const p2 = priorityOrder[t2.priority] || 1;
    
    
    // Compare by priority first (higher priority first)
    if (p1 !== p2) {
        return p2 - p1;
    }
    
    
    // JavaScript: Compare by timestamp if priorities are equal
    return t1.timestamp - t2.timestamp;
}

function sortStringsCustom(strings) {
    
    // JavaScript: Array.sort() with custom comparator
    return [...strings].sort(customStringComparator);
}

function sortPeopleMultiCriteria(people) {
    
    // JavaScript: Sort using multi-criteria comparator
    return [...people].sort(personComparator);
}

function sortTasksByPriority(tasks) {
    
    // JavaScript: Sort using priority-based comparator
    return [...tasks].sort(taskComparator);
}

function findKthElement(arr, k, comparator = (a, b) => a - b) {
    
    // JavaScript: Sort with custom comparator and return kth element
    const sorted = [...arr].sort(comparator);
    
    if (k >= 1 && k <= sorted.length) {
        return sorted[k - 1];
    }
    return null;
}

function mergeSortedArrays(arr1, arr2, comparator = (a, b) => a - b) {
    
    // JavaScript: Merge two sorted arrays using comparator
    const result = [];
    let i = 0, j = 0;
    
    while (i < arr1.length && j < arr2.length) {
        if (comparator(arr1[i], arr2[j]) <= 0) {
            result.push(arr1[i]);
            i++;
        } else {
            result.push(arr2[j]);
            j++;
        }
    }
    
    
    // JavaScript: Add remaining elements using spread operator
    result.push(...arr1.slice(i));
    result.push(...arr2.slice(j));
    
    return result;
}

function binarySearchWithComparator(arr, target, comparator) {
    
    // JavaScript: Binary search with custom comparator
    let left = 0, right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const comparison = comparator(arr[mid], target);
        
        if (comparison === 0) {
            return mid;
        } else if (comparison < 0) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

function sortByMultipleCriteria(data, criteria) {
    
    // JavaScript: Generic multi-criteria sorting function
    return [...data].sort((a, b) => {
        for (const criterion of criteria) {
            const { key, order = 'asc' } = criterion;
            const aVal = a[key];
            const bVal = b[key];
            
            let comparison = 0;
            if (typeof aVal === 'string') {
                comparison = aVal.localeCompare(bVal);
            } else {
                comparison = aVal - bVal;
            }
            
            if (comparison !== 0) {
                return order === 'desc' ? -comparison : comparison;
            }
        }
        return 0;
    });
}

function createComparator(keyExtractor, reverse = false) {
    
    // JavaScript: Higher-order function to create comparators
    return function(a, b) {
        const aKey = keyExtractor(a);
        const bKey = keyExtractor(b);
        
        let result = 0;
        if (typeof aKey === 'string') {
            result = aKey.localeCompare(bKey);
        } else {
            result = aKey - bKey;
        }
        
        return reverse ? -result : result;
    };
}

// Test the comparator logic
const strings = ["apple", "pie", "a", "longer", "cat"];
const sortedStrings = sortStringsCustom(strings);
console.log("Custom sorted strings:", sortedStrings);


// Test multi-criteria person sorting
const people = [
    { name: 'Alice', age: 30, score: 85 },
    { name: 'Bob', age: 25, score: 90 },
    { name: 'Charlie', age: 25, score: 95 },
    { name: 'Alice', age: 30, score: 80 }
];

const sortedPeople = sortPeopleMultiCriteria(people);
console.log("\nSorted people:");
sortedPeople.forEach(person => console.log("  ", person));


// Test priority-based task sorting
const tasks = [
    { name: 'Task1', priority: 'low', timestamp: 100 },
    { name: 'Task2', priority: 'high', timestamp: 50 },
    { name: 'Task3', priority: 'medium', timestamp: 75 },
    { name: 'Task4', priority: 'high', timestamp: 25 }
];

const sortedTasks = sortTasksByPriority(tasks);
console.log("\nSorted tasks by priority:");
sortedTasks.forEach(task => console.log("  ", task));


// Test kth element finding
const numbers = [64, 34, 25, 12, 22, 11, 90];
const kthElement = findKthElement(numbers, 3);
console.log("\n3rd smallest element:", kthElement);


// Test merging sorted arrays
const arr1 = [1, 3, 5, 7];
const arr2 = [2, 4, 6, 8];
const merged = mergeSortedArrays(arr1, arr2);
console.log("\nMerged arrays:", merged);


// Test generic multi-criteria sorting
const employees = [
    { name: 'John', department: 'IT', salary: 75000, experience: 5 },
    { name: 'Jane', department: 'HR', salary: 65000, experience: 3 },
    { name: 'Bob', department: 'IT', salary: 80000, experience: 7 },
    { name: 'Alice', department: 'HR', salary: 70000, experience: 4 }
];

const sortCriteria = [
    { key: 'department', order: 'asc' },
    { key: 'salary', order: 'desc' },
    { key: 'experience', order: 'desc' }
];

const sortedEmployees = sortByMultipleCriteria(employees, sortCriteria);
console.log("\nSorted employees by department, salary (desc), experience (desc):");
sortedEmployees.forEach(emp => console.log("  ", emp));
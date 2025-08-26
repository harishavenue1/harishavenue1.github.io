function generateTestCases(inputRanges, constraints = null) {
    
    // JavaScript: Initialize test case collections
    const testCases = [];
    
    // JavaScript: Generate different types of test cases
    const boundaryCases = generateBoundaryCases(inputRanges);
    const equivalenceCases = generateEquivalenceCases(inputRanges);
    const edgeCases = generateEdgeCases(inputRanges, constraints);
    
    
    // JavaScript: Combine all test case types using spread operator
    testCases.push(...boundaryCases, ...equivalenceCases, ...edgeCases);
    
    return removeDuplicates(testCases);
}

function generateBoundaryCases(inputRanges) {
    
    // JavaScript: Array to store boundary test cases
    const cases = [];
    
    for (const [param, [minVal, maxVal]] of Object.entries(inputRanges)) {
        
        // Test boundary values
        cases.push({ [param]: minVal, test_type: 'boundary_min' });
        cases.push({ [param]: maxVal, test_type: 'boundary_max' });
        cases.push({ [param]: minVal - 1, test_type: 'boundary_below_min' });
        cases.push({ [param]: maxVal + 1, test_type: 'boundary_above_max' });
        
        
        // JavaScript: Math.floor() for integer division
        const midVal = Math.floor((minVal + maxVal) / 2);
        cases.push({ [param]: midVal, test_type: 'boundary_mid' });
    }
    
    return cases;
}

function generateEquivalenceCases(inputRanges) {
    
    // JavaScript: Array to store equivalence test cases
    const cases = [];
    
    for (const [param, [minVal, maxVal]] of Object.entries(inputRanges)) {
        
        // Valid equivalence class
        const validVal = minVal + Math.floor((maxVal - minVal) / 3);
        cases.push({ [param]: validVal, test_type: 'equivalence_valid' });
        
        
        // Invalid equivalence classes
        cases.push({ [param]: minVal - 10, test_type: 'equivalence_invalid_low' });
        cases.push({ [param]: maxVal + 10, test_type: 'equivalence_invalid_high' });
    }
    
    return cases;
}

function generateEdgeCases(inputRanges, constraints) {
    
    // JavaScript: Array to store edge test cases
    const cases = [];
    
    
    // JavaScript: Generate null/empty cases
    cases.push({ input: null, test_type: 'edge_null' });
    cases.push({ input: '', test_type: 'edge_empty' });
    cases.push({ input: 0, test_type: 'edge_zero' });
    cases.push({ input: -1, test_type: 'edge_negative' });
    
    
    // JavaScript: Generate constraint-based cases if provided
    if (constraints) {
        for (const [constraintType, constraintValue] of Object.entries(constraints)) {
            if (constraintType === 'max_length') {
                
                // Test maximum length boundary
                cases.push({
                    input: 'x'.repeat(constraintValue),
                    test_type: `edge_max_length_${constraintValue}`
                });
                
                // Test exceeding maximum length
                cases.push({
                    input: 'x'.repeat(constraintValue + 1),
                    test_type: `edge_exceed_length_${constraintValue}`
                });
            }
        }
    }
    
    return cases;
}

function removeDuplicates(testCases) {
    
    // JavaScript: Set to track seen test cases using JSON.stringify
    const seen = new Set();
    const uniqueCases = [];
    
    for (const testCase of testCases) {
        
        // JavaScript: Convert object to string for comparison
        const caseKey = JSON.stringify(testCase);
        
        if (!seen.has(caseKey)) {
            seen.add(caseKey);
            uniqueCases.push(testCase);
        }
    }
    
    return uniqueCases;
}

function analyzeCoverage(testCases, requirements) {
    
    // JavaScript: Object to track coverage metrics
    const coverageReport = {
        total_test_cases: testCases.length,
        boundary_coverage: 0,
        equivalence_coverage: 0,
        edge_case_coverage: 0,
        requirement_coverage: {}
    };
    
    
    // JavaScript: Count test case types
    for (const testCase of testCases) {
        const testType = testCase.test_type || '';
        
        if (testType.includes('boundary')) {
            coverageReport.boundary_coverage++;
        } else if (testType.includes('equivalence')) {
            coverageReport.equivalence_coverage++;
        } else if (testType.includes('edge')) {
            coverageReport.edge_case_coverage++;
        }
    }
    
    
    // JavaScript: Calculate coverage percentages
    const total = coverageReport.total_test_cases;
    if (total > 0) {
        coverageReport.boundary_percentage = (coverageReport.boundary_coverage / total) * 100;
        coverageReport.equivalence_percentage = (coverageReport.equivalence_coverage / total) * 100;
        coverageReport.edge_percentage = (coverageReport.edge_case_coverage / total) * 100;
    }
    
    return coverageReport;
}

// Test the Test Case Generator
const inputRanges = {
    username_length: [3, 20],
    password_length: [8, 50],
    age: [18, 120]
};

const constraints = {
    max_length: 255,
    special_chars: true
};

const testCases = generateTestCases(inputRanges, constraints);
console.log(`Generated ${testCases.length} test cases:`);

testCases.slice(0, 10).forEach((testCase, i) => {
    console.log(`${i + 1}. ${JSON.stringify(testCase)}`);
});

const coverage = analyzeCoverage(testCases, ['login', 'validation', 'security']);
console.log(`\nTest Coverage Analysis:`);
console.log(`Total Test Cases: ${coverage.total_test_cases}`);
console.log(`Boundary Coverage: ${coverage.boundary_percentage?.toFixed(1) || 0}%`);
console.log(`Equivalence Coverage: ${coverage.equivalence_percentage?.toFixed(1) || 0}%`);
console.log(`Edge Case Coverage: ${coverage.edge_percentage?.toFixed(1) || 0}%`);
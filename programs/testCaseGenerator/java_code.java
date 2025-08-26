import java.util.*;

public class TestCaseGenerator {
    
    public static List<Map<String, Object>> generateTestCases(Map<String, int[]> inputRanges, Map<String, Object> constraints) {
        
        // Java: ArrayList to store all test cases
        List<Map<String, Object>> testCases = new ArrayList<>();
        
        // Java: Generate different types of test cases
        testCases.addAll(generateBoundaryCases(inputRanges));
        testCases.addAll(generateEquivalenceCases(inputRanges));
        testCases.addAll(generateEdgeCases(inputRanges, constraints));
        
        return removeDuplicates(testCases);
    }
    
    private static List<Map<String, Object>> generateBoundaryCases(Map<String, int[]> inputRanges) {
        
        // Java: List to store boundary test cases
        List<Map<String, Object>> cases = new ArrayList<>();
        
        for (Map.Entry<String, int[]> entry : inputRanges.entrySet()) {
            String param = entry.getKey();
            int[] range = entry.getValue();
            int minVal = range[0];
            int maxVal = range[1];
            
            
            // Java: HashMap for each test case
            cases.add(createTestCase(param, minVal, "boundary_min"));
            cases.add(createTestCase(param, maxVal, "boundary_max"));
            cases.add(createTestCase(param, minVal - 1, "boundary_below_min"));
            cases.add(createTestCase(param, maxVal + 1, "boundary_above_max"));
            
            
            // Java: Integer division for mid value
            int midVal = (minVal + maxVal) / 2;
            cases.add(createTestCase(param, midVal, "boundary_mid"));
        }
        
        return cases;
    }
    
    private static List<Map<String, Object>> generateEquivalenceCases(Map<String, int[]> inputRanges) {
        
        // Java: List to store equivalence test cases
        List<Map<String, Object>> cases = new ArrayList<>();
        
        for (Map.Entry<String, int[]> entry : inputRanges.entrySet()) {
            String param = entry.getKey();
            int[] range = entry.getValue();
            int minVal = range[0];
            int maxVal = range[1];
            
            
            // Valid equivalence class
            int validVal = minVal + (maxVal - minVal) / 3;
            cases.add(createTestCase(param, validVal, "equivalence_valid"));
            
            
            // Invalid equivalence classes
            cases.add(createTestCase(param, minVal - 10, "equivalence_invalid_low"));
            cases.add(createTestCase(param, maxVal + 10, "equivalence_invalid_high"));
        }
        
        return cases;
    }
    
    private static List<Map<String, Object>> generateEdgeCases(Map<String, int[]> inputRanges, Map<String, Object> constraints) {
        
        // Java: List to store edge test cases
        List<Map<String, Object>> cases = new ArrayList<>();
        
        
        // Java: Generate null/empty cases
        cases.add(createTestCase("input", null, "edge_null"));
        cases.add(createTestCase("input", "", "edge_empty"));
        cases.add(createTestCase("input", 0, "edge_zero"));
        cases.add(createTestCase("input", -1, "edge_negative"));
        
        
        // Java: Generate constraint-based cases if provided
        if (constraints != null && constraints.containsKey("max_length")) {
            int maxLength = (Integer) constraints.get("max_length");
            
            
            // Java: StringBuilder.repeat() for string repetition (Java 11+)
            String maxLengthStr = "x".repeat(maxLength);
            cases.add(createTestCase("input", maxLengthStr, "edge_max_length_" + maxLength));
            
            String exceedLengthStr = "x".repeat(maxLength + 1);
            cases.add(createTestCase("input", exceedLengthStr, "edge_exceed_length_" + maxLength));
        }
        
        return cases;
    }
    
    private static Map<String, Object> createTestCase(String key, Object value, String testType) {
        
        // Java: HashMap to represent a test case
        Map<String, Object> testCase = new HashMap<>();
        testCase.put(key, value);
        testCase.put("test_type", testType);
        return testCase;
    }
    
    private static List<Map<String, Object>> removeDuplicates(List<Map<String, Object>> testCases) {
        
        // Java: LinkedHashSet to maintain order while removing duplicates
        Set<String> seen = new HashSet<>();
        List<Map<String, Object>> uniqueCases = new ArrayList<>();
        
        for (Map<String, Object> testCase : testCases) {
            
            // Java: Convert map to string for comparison
            String caseKey = testCase.toString();
            
            if (!seen.contains(caseKey)) {
                seen.add(caseKey);
                uniqueCases.add(testCase);
            }
        }
        
        return uniqueCases;
    }
    
    public static Map<String, Object> analyzeCoverage(List<Map<String, Object>> testCases, List<String> requirements) {
        
        // Java: HashMap to track coverage metrics
        Map<String, Object> coverageReport = new HashMap<>();
        coverageReport.put("total_test_cases", testCases.size());
        coverageReport.put("boundary_coverage", 0);
        coverageReport.put("equivalence_coverage", 0);
        coverageReport.put("edge_case_coverage", 0);
        
        
        // Java: Count test case types
        int boundaryCount = 0, equivalenceCount = 0, edgeCount = 0;
        
        for (Map<String, Object> testCase : testCases) {
            String testType = (String) testCase.getOrDefault("test_type", "");
            
            if (testType.contains("boundary")) {
                boundaryCount++;
            } else if (testType.contains("equivalence")) {
                equivalenceCount++;
            } else if (testType.contains("edge")) {
                edgeCount++;
            }
        }
        
        coverageReport.put("boundary_coverage", boundaryCount);
        coverageReport.put("equivalence_coverage", equivalenceCount);
        coverageReport.put("edge_case_coverage", edgeCount);
        
        
        // Java: Calculate coverage percentages
        int total = testCases.size();
        if (total > 0) {
            coverageReport.put("boundary_percentage", (boundaryCount * 100.0) / total);
            coverageReport.put("equivalence_percentage", (equivalenceCount * 100.0) / total);
            coverageReport.put("edge_percentage", (edgeCount * 100.0) / total);
        }
        
        return coverageReport;
    }
    
    public static void main(String[] args) {
        
        // Define input ranges for testing
        Map<String, int[]> inputRanges = new HashMap<>();
        inputRanges.put("username_length", new int[]{3, 20});
        inputRanges.put("password_length", new int[]{8, 50});
        inputRanges.put("age", new int[]{18, 120});
        
        Map<String, Object> constraints = new HashMap<>();
        constraints.put("max_length", 255);
        constraints.put("special_chars", true);
        
        
        // Generate comprehensive test cases
        List<Map<String, Object>> testCases = generateTestCases(inputRanges, constraints);
        
        System.out.println("Generated " + testCases.size() + " test cases:");
        for (int i = 0; i < Math.min(10, testCases.size()); i++) {
            System.out.println((i + 1) + ". " + testCases.get(i));
        }
        
        
        // Analyze test coverage
        List<String> requirements = Arrays.asList("login", "validation", "security");
        Map<String, Object> coverage = analyzeCoverage(testCases, requirements);
        
        System.out.println("\nTest Coverage Analysis:");
        System.out.println("Total Test Cases: " + coverage.get("total_test_cases"));
        System.out.printf("Boundary Coverage: %.1f%%\n", (Double) coverage.getOrDefault("boundary_percentage", 0.0));
        System.out.printf("Equivalence Coverage: %.1f%%\n", (Double) coverage.getOrDefault("equivalence_percentage", 0.0));
        System.out.printf("Edge Case Coverage: %.1f%%\n", (Double) coverage.getOrDefault("edge_percentage", 0.0));
    }
}
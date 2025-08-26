using System;
using System.Collections.Generic;
using System.Linq;

public class TestCaseGenerator
{
    public static List<Dictionary<string, object>> GenerateTestCases(Dictionary<string, int[]> inputRanges, Dictionary<string, object> constraints = null)
    {
        
        // C#: List to store all test cases
        var testCases = new List<Dictionary<string, object>>();
        
        // C#: Generate different types of test cases
        testCases.AddRange(GenerateBoundaryCases(inputRanges));
        testCases.AddRange(GenerateEquivalenceCases(inputRanges));
        testCases.AddRange(GenerateEdgeCases(inputRanges, constraints));
        
        return RemoveDuplicates(testCases);
    }
    
    private static List<Dictionary<string, object>> GenerateBoundaryCases(Dictionary<string, int[]> inputRanges)
    {
        
        // C#: List to store boundary test cases
        var cases = new List<Dictionary<string, object>>();
        
        foreach (var kvp in inputRanges)
        {
            string param = kvp.Key;
            int[] range = kvp.Value;
            int minVal = range[0];
            int maxVal = range[1];
            
            
            // C#: Dictionary for each test case
            cases.Add(CreateTestCase(param, minVal, "boundary_min"));
            cases.Add(CreateTestCase(param, maxVal, "boundary_max"));
            cases.Add(CreateTestCase(param, minVal - 1, "boundary_below_min"));
            cases.Add(CreateTestCase(param, maxVal + 1, "boundary_above_max"));
            
            
            // C#: Integer division for mid value
            int midVal = (minVal + maxVal) / 2;
            cases.Add(CreateTestCase(param, midVal, "boundary_mid"));
        }
        
        return cases;
    }
    
    private static List<Dictionary<string, object>> GenerateEquivalenceCases(Dictionary<string, int[]> inputRanges)
    {
        
        // C#: List to store equivalence test cases
        var cases = new List<Dictionary<string, object>>();
        
        foreach (var kvp in inputRanges)
        {
            string param = kvp.Key;
            int[] range = kvp.Value;
            int minVal = range[0];
            int maxVal = range[1];
            
            
            // Valid equivalence class
            int validVal = minVal + (maxVal - minVal) / 3;
            cases.Add(CreateTestCase(param, validVal, "equivalence_valid"));
            
            
            // Invalid equivalence classes
            cases.Add(CreateTestCase(param, minVal - 10, "equivalence_invalid_low"));
            cases.Add(CreateTestCase(param, maxVal + 10, "equivalence_invalid_high"));
        }
        
        return cases;
    }
    
    private static List<Dictionary<string, object>> GenerateEdgeCases(Dictionary<string, int[]> inputRanges, Dictionary<string, object> constraints)
    {
        
        // C#: List to store edge test cases
        var cases = new List<Dictionary<string, object>>();
        
        
        // C#: Generate null/empty cases
        cases.Add(CreateTestCase("input", null, "edge_null"));
        cases.Add(CreateTestCase("input", "", "edge_empty"));
        cases.Add(CreateTestCase("input", 0, "edge_zero"));
        cases.Add(CreateTestCase("input", -1, "edge_negative"));
        
        
        // C#: Generate constraint-based cases if provided
        if (constraints != null && constraints.ContainsKey("max_length"))
        {
            int maxLength = (int)constraints["max_length"];
            
            
            // C#: new string() constructor for string repetition
            string maxLengthStr = new string('x', maxLength);
            cases.Add(CreateTestCase("input", maxLengthStr, $"edge_max_length_{maxLength}"));
            
            string exceedLengthStr = new string('x', maxLength + 1);
            cases.Add(CreateTestCase("input", exceedLengthStr, $"edge_exceed_length_{maxLength}"));
        }
        
        return cases;
    }
    
    private static Dictionary<string, object> CreateTestCase(string key, object value, string testType)
    {
        
        // C#: Dictionary to represent a test case
        return new Dictionary<string, object>
        {
            { key, value },
            { "test_type", testType }
        };
    }
    
    private static List<Dictionary<string, object>> RemoveDuplicates(List<Dictionary<string, object>> testCases)
    {
        
        // C#: HashSet to track seen test cases
        var seen = new HashSet<string>();
        var uniqueCases = new List<Dictionary<string, object>>();
        
        foreach (var testCase in testCases)
        {
            
            // C#: Convert dictionary to string for comparison
            string caseKey = string.Join(",", testCase.Select(kvp => $"{kvp.Key}:{kvp.Value}"));
            
            if (!seen.Contains(caseKey))
            {
                seen.Add(caseKey);
                uniqueCases.Add(testCase);
            }
        }
        
        return uniqueCases;
    }
    
    public static Dictionary<string, object> AnalyzeCoverage(List<Dictionary<string, object>> testCases, List<string> requirements)
    {
        
        // C#: Dictionary to track coverage metrics
        var coverageReport = new Dictionary<string, object>
        {
            ["total_test_cases"] = testCases.Count,
            ["boundary_coverage"] = 0,
            ["equivalence_coverage"] = 0,
            ["edge_case_coverage"] = 0
        };
        
        
        // C#: Count test case types using LINQ
        int boundaryCount = testCases.Count(tc => tc.ContainsKey("test_type") && tc["test_type"].ToString().Contains("boundary"));
        int equivalenceCount = testCases.Count(tc => tc.ContainsKey("test_type") && tc["test_type"].ToString().Contains("equivalence"));
        int edgeCount = testCases.Count(tc => tc.ContainsKey("test_type") && tc["test_type"].ToString().Contains("edge"));
        
        coverageReport["boundary_coverage"] = boundaryCount;
        coverageReport["equivalence_coverage"] = equivalenceCount;
        coverageReport["edge_case_coverage"] = edgeCount;
        
        
        // C#: Calculate coverage percentages
        int total = testCases.Count;
        if (total > 0)
        {
            coverageReport["boundary_percentage"] = (boundaryCount * 100.0) / total;
            coverageReport["equivalence_percentage"] = (equivalenceCount * 100.0) / total;
            coverageReport["edge_percentage"] = (edgeCount * 100.0) / total;
        }
        
        return coverageReport;
    }
    
    public static void Main(string[] args)
    {
        
        // Define input ranges for testing
        var inputRanges = new Dictionary<string, int[]>
        {
            ["username_length"] = new int[] { 3, 20 },
            ["password_length"] = new int[] { 8, 50 },
            ["age"] = new int[] { 18, 120 }
        };
        
        var constraints = new Dictionary<string, object>
        {
            ["max_length"] = 255,
            ["special_chars"] = true
        };
        
        
        // Generate comprehensive test cases
        var testCases = GenerateTestCases(inputRanges, constraints);
        
        Console.WriteLine($"Generated {testCases.Count} test cases:");
        for (int i = 0; i < Math.Min(10, testCases.Count); i++)
        {
            var testCase = testCases[i];
            var caseStr = string.Join(", ", testCase.Select(kvp => $"{kvp.Key}: {kvp.Value}"));
            Console.WriteLine($"{i + 1}. {{{caseStr}}}");
        }
        
        
        // Analyze test coverage
        var requirements = new List<string> { "login", "validation", "security" };
        var coverage = AnalyzeCoverage(testCases, requirements);
        
        Console.WriteLine($"\nTest Coverage Analysis:");
        Console.WriteLine($"Total Test Cases: {coverage["total_test_cases"]}");
        Console.WriteLine($"Boundary Coverage: {coverage.GetValueOrDefault("boundary_percentage", 0.0):F1}%");
        Console.WriteLine($"Equivalence Coverage: {coverage.GetValueOrDefault("equivalence_percentage", 0.0):F1}%");
        Console.WriteLine($"Edge Case Coverage: {coverage.GetValueOrDefault("edge_percentage", 0.0):F1}%");
    }
}
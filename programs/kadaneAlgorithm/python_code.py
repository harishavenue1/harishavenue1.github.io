# Kadane's Algorithm for Maximum Subarray Sum
def kadane_algorithm(arr):
    """Basic Kadane's Algorithm"""
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    print("\nKadane's Algorithm step by step:")
    print(f"Initial: max_sum={max_sum}, current_sum={current_sum}")
    
    for i in range(1, len(arr)):
        # Either extend the existing subarray or start a new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
        
        print(f"i={i}, arr[{i}]={arr[i]}, current_sum={current_sum}, max_sum={max_sum}")
    
    return max_sum

def kadane_with_indices(arr):
    """Kadane's Algorithm with subarray indices"""
    if not arr:
        return 0, 0, 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

def kadane_pythonic(arr):
    """Pythonic approach using itertools.accumulate"""
    if not arr:
        return 0
    
    from itertools import accumulate
    
    # Generate all possible current sums
    current_sums = list(accumulate(arr, lambda acc, x: max(x, acc + x)))
    return max(current_sums)

def kadane_with_dp(arr):
    """Dynamic Programming approach (explicit)"""
    if not arr:
        return 0
    
    n = len(arr)
    dp = [0] * n  # dp[i] = max sum ending at index i
    dp[0] = arr[0]
    max_sum = arr[0]
    
    print("\nDP approach:")
    print(f"dp[0] = {dp[0]}")
    
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
        max_sum = max(max_sum, dp[i])
        print(f"dp[{i}] = max({arr[i]}, {dp[i-1]} + {arr[i]}) = {dp[i]}")
    
    print(f"DP array: {dp}")
    return max_sum

# Main execution
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Array:", arr)
    
    # Basic algorithm
    max_sum = kadane_algorithm(arr)
    print(f"Maximum subarray sum: {max_sum}")
    
    # With indices
    max_sum, start, end = kadane_with_indices(arr)
    print(f"Max sum: {max_sum}, Start: {start}, End: {end}")
    print(f"Subarray: {arr[start:end+1]}")
    
    # Pythonic approach
    pythonic_result = kadane_pythonic(arr)
    print(f"Pythonic result: {pythonic_result}")
    
    # DP approach
    dp_result = kadane_with_dp(arr)
    print(f"DP result: {dp_result}")
    
    # Handle all negative numbers
    negative_arr = [-5, -2, -8, -1, -4]
    print(f"\nAll negative array: {negative_arr}")
    
    def kadane_all_negative(arr):
        if not arr:
            return 0
        # If all numbers are negative, return the maximum single element
        if all(x < 0 for x in arr):
            return max(arr)
        return kadane_algorithm(arr)
    
    print(f"Max sum (all negative): {kadane_all_negative(negative_arr)}")
    
    # List comprehension approach
    def kadane_comprehension(arr):
        if not arr:
            return 0
        
        max_ending_here = max_so_far = arr[0]
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    print(f"Comprehension result: {kadane_comprehension(arr)}")
    
    # Using numpy (if available)
    try:
        import numpy as np
        arr_np = np.array(arr)
        print(f"NumPy array: {arr_np}")
        print(f"NumPy max: {kadane_algorithm(arr_np.tolist())}")
    except ImportError:
        print("NumPy not available")
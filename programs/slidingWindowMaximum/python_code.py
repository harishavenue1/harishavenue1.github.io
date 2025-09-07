def sliding_window_max_sum(arr, k):
    """Sliding Window Maximum Sum - O(n) optimized"""
    n = len(arr)
    
    # Calculate first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    print("\n=== SLIDING WINDOW MAXIMUM SUM ===")
    print(f"Window [0-{k-1}]: Sum = {window_sum}")
    
    # Slide the window
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]  # Remove left, add right
        print(f"Window [{i - k + 1}-{i}]: Sum = {window_sum}", end="")
        
        if window_sum > max_sum:
            max_sum = window_sum
            print(" <- NEW MAX!")
        else:
            print()
    
    return max_sum

# Main execution
if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    
    print("Array:", arr)
    print("Window size:", window_size)
    
    max_sum = sliding_window_max_sum(arr, window_size)
    print(f"\nMaximum sum of any window: {max_sum}")
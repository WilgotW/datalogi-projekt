def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        mid_value = sorted_list[mid]

        # Check if we found the target
        if mid_value == target:
            return mid  # Return the index where it was found
            
        # If target is greater, ignore the left half
        elif mid_value < target:
            left = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # If we get out of the loop, the target isn't in the list
    return -1

# --- Example Usage ---
my_sorted_list = [3, 9, 10, 27, 38, 43, 82]
target_number = 43

result_index = binary_search(my_sorted_list, target_number)

if result_index != -1:
    print(f"Found {target_number} at index {result_index}!")
else:
    print("Target not found in the list.")
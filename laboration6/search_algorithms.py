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


def linear_search(any_list, target):
    # Enumerate gives us both the index (i) and the actual value (item)
    for i, item in enumerate(any_list):
        if item == target:
            return i  # Return the index where it was found
            
    return -1  # If the loop finishes without returning, it's not in the list
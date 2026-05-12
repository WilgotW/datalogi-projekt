#Kod skapad av Gemini. 

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE
    # Find the middle point and split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 2. CONQUER (Merge)
    # Merge the now-sorted halves together
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    i = 0  # Index for the left half
    j = 0  # Index for the right half

    # Compare elements from both halves until one half is empty
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are any leftover elements in the left half, add them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are any leftover elements in the right half, add them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

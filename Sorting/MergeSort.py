def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged_arr = merge(left_half, right_half)

    return merged_arr

def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add the remaining elements (if any) from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Taking input from the keyboard
input_list = list(map(int, input("Enter space-separated numbers: ").split()))

# Applying merge sort
sorted_list = merge_sort(input_list)

# Print the sorted output
print("Sorted list:", sorted_list)

def insertion_sort(arr):
    """
    Perform Insertion Sort on the given list.

    Parameters:
    - arr (list): List of comparable elements to be sorted in-place.
    """
    n = len(arr)

    # Traverse through all array elements starting from the second element
    for i in range(1, n):
        # Save the current element to be inserted into the sorted part
        current_element = arr[i]

        # Move elements of the sorted part that are greater than the current element
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into the correct position in the sorted part
        arr[j + 1] = current_element

# Taking input from the keyboard
input_list = list(map(int, input("Enter space-separated numbers: ").split()))

# Applying insertion sort
insertion_sort(input_list)

# Print the sorted output
print("Sorted list:", input_list)

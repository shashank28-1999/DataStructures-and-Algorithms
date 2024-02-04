def selection_sort(arr):
    """
    Selection Sort algorithm: repeatedly finds the minimum element from the unsorted part
    and puts it at the beginning.

    :param arr: List of comparable elements
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input from the keyboard
input_list = list(map(int, input("Enter space-separated numbers: ").split()))

# Applying selection sort
selection_sort(input_list)

# Print the sorted output
print("Sorted list:", input_list)

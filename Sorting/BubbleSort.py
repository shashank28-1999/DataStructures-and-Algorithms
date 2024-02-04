def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if(arr[i]<arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr

# Taking input from the keyboard
input_list = list(map(int, input("Enter space-separated numbers: ").split()))

# Applying bubble sort
sorted_list = bubble_sort(input_list)

# Print the sorted output
print("Sorted list:", sorted_list)

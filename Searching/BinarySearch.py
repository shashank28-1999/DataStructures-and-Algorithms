"""
    Perform binary search on a sorted array using recursion.

    Parameters:
    - arr: A sorted list.
    - target: The element to search for.
    - low: The starting index of the current search range.
    - high: The ending index of the current search range.

    Returns:
    - The index of the target element if found, otherwise -1.
    """
def binarySearch(l,search,low,high):
    if(low<=high):
        mid=(low+high)//2
        if(l[mid]==search):
            return mid
        if(l[mid] > search):
            return binarySearch(l,search,low,mid-1)
        else:
            return binarySearch(l,search,mid+1,high)
    else:
       return -1
a=[]
n=int(input("Enter size of list: "))
print("Enter list elements")
for i in range(0,n):
    x=int(input())
    a.append(x)
print("Enter element to be searched: ")
s=int(input())
ans=binarySearch(a,s,0,n-1)

if ans!=-1:
    print("element found at index: ",ans)
else:
    print("element not present in the list")

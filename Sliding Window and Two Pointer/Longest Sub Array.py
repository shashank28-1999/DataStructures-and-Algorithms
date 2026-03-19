# This code gives you the longest sub array whose sum is less than or equal to the target
print("enter the length of the array")
n=int(input())
print("Enter elements of the array")
l = list(map(int, input().split()))
if len(l) != n:
    print(f"Error: Expected {n} numbers, but got {len(l)}.")
else:
    print("enter the target")
target=int(input())
left=0
right=0
maxlength=0
x=0
y=0
z=0
while(right<n):
    x=x+l[right]
    while(x>target):
        x=x-l[left]
        left=left+1
    if(x<=target and right-left+1>maxlength):
        maxlength=right-left+1
        y=left
        z=right+1
    right=right+1
print("length of longest sub array is ",maxlength)
ans=[]
print("Longest subarray is ")
for i in range(y,z):
    ans.append(l[i])
print(ans)

    

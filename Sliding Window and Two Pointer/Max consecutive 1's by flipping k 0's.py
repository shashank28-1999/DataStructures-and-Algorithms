# Array contains 1's and 0's achieve at maximum consecutive 1's by flipping k zeros
print("enter your array with 0's and 1's")
l = list(map(int, input().split()))
print("number of 0's to be flipped")
k=int(input())
left=0
right=0
number_of_zeros=0
maxlength=0
while(right<len(l)):
    if(l[right]==0):
        number_of_zeros=number_of_zeros+1
    if(number_of_zeros>k):
        if(l[left]==0):
            number_of_zeros=number_of_zeros-1
        left=left-1
    if(number_of_zeros<=k):
        maxlength=max(maxlength,right-left+1)
    right=right+1
print("maximum length of array is ",maxlength)
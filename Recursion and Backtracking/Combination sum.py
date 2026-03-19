#Return list of all combinations which is equal to target k
# you can use a number multiple times
print("enter the list")
inp=list(map(int, input().split()))
print("enter target")
k=int(input())

def findCombinations(index,arr,target,l,x):
    if(index==len(arr)):
        if(target==0):
            l.append(list(x)) # x.copy() also works because x is argument and keeps changing
        return
    if(arr[index]<=target):
        x.append(arr[index])
        findCombinations(index,arr,target-arr[index],l,x)
        del x[-1] #we can also use x.pop()
    findCombinations(index+1,arr,target,l,x)

l=[]
x=[]
findCombinations(0,inp,k,l,x)

print("combinations are:")
print(l)
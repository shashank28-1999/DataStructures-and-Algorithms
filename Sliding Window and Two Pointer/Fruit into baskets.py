#pick maximum fruits which fit into 2 baskets (each basket has infinite space)
#you are only allowed to pick in a sequence
from collections import defaultdict
print("enter the array")
l=list(map(int,input().split()))
left=0
right=0
maxlength=0
hash_map=defaultdict(int)
while(right<len(l)):
    hash_map[l[right]]=hash_map[l[right]]+1
    if(len(hash_map)>2):
        hash_map[l[left]]=hash_map[l[left]]-1
        if(hash_map[l[left]]==0):
            del hash_map[left]
        left=left+1
    if(len(hash_map)<=2):
        maxlength=max(maxlength,right-left+1)
    right=right+1
print("max length is ",maxlength)
    


#longest substring with atmost k distinct characters
from collections import defaultdict
print("enter the string")
s=input()
left=0
right=0
maxlength=0
d=defaultdict(int)
print("enter number of distinct characters")
k=int(input())
while(right<len(s)):
    d[s[right]]=d[s[right]]+1
    if(len(d)>k):
        d[s[left]]=d[s[left]]-1
        if(d[s[left]]==0):
            del d[s[left]]
        left=left+1
    if(len(d)<=k):
        maxlength=max(maxlength,right-left+1)
    right=right+1
print(f"maximum length of substring with atmost {k} consecutive characters is {maxlength}")
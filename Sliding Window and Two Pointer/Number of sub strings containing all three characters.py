#number of substrings containing all three characters (a,b,c)
print("enter the string using a,b,c only")
s=input()
last_seen=[-1,-1,-1]
count=0
for i in range(0,len(s)):
    last_seen[ord(s[i])-ord('a')]=i
    count=count+(1+min(last_seen[0],last_seen[1],last_seen[2]))
print("number of substrings are ",count)

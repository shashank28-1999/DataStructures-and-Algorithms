# Return the longest substring with no repeating chracters
print("enter the string")
input_string=input()
char_index={}
#using dictionary to represent a hashmap
left=0
start=0
maxlength=0
for right in range(0,len(input_string)):
    ch=input_string[right]
    if (ch in char_index and char_index[ch]>=left):
        left=char_index[ch]+1
    char_index[ch]=right
    if(right-left+1>maxlength):
        maxlength=right-left+1
        start=left
print("longest sub string is ",input_string[start:start+maxlength])
print("length is ",maxlength)
print(char_index)
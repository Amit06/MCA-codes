 # Paste your code into this box 
s=raw_input()

p=''
k=''
for i in range(len(s)):
    j=i
    k+=s[j]
    while j<len(s)-1 and s[j]<=s[j+1]:
        k+=s[j+1]
        j+=1
    if len(k)>len(p):
        p=k
    k=''
print p
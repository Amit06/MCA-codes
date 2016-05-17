from random import randint
"" "Question 9 : Data Structures in C"""
def no0(a):
    for i in a:
        for j in i:
            if j==0:
                return True
    return False
n,m=map(int,raw_input().split())
counter=[]
for i in range(n):
    c=[]
    for j in range(m):
        c.append(0)
    counter.append(c)

#imoves construction

imove=[-1,0,1,1,1,0,-1,-1]
jmove=[1,1,1,0,-1,-1,-1,0]

i,j=map(int,raw_input().split())

counter[i][j]=1
#print counter

test=1
while test<=50000 and no0(counter) :
    k=randint(0,7)
    
    if i+imove[k]<n and j+jmove[k]<m and i+imove[k]>=0 and j+jmove[k]>=0:
        i=i+imove[k]
        j=j+jmove[k]
       
        counter[i][j]+=1
        for c in counter:
            print c
        print "\n\n"
    test+=1
    
print test
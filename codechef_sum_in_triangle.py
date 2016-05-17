import sys
tc=input()
a=[]
k=0

while tc>0:
    no_of_lines=input()
    k=no_of_lines
    #print "k is "+str(k)
    while no_of_lines>0:
        lines=map(int,raw_input().split())
        a.append(lines)
        
        no_of_lines-=1
    for i in reversed(range(k-1)):
        #print "i is:"+str(i)
        for j in range(i+1):
            #print "j is:"+str(j)
            a[i][j]+=a[i+1][j] if a[i+1][j]>a[i+1][j+1] else a[i+1][j+1]
    print a[0][0]
    
    a=[]
    tc-=1
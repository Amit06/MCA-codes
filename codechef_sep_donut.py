'''
    @author:ph0enix
'''

test=input()

while test>0:
    ctr=0
    chains=[]
    o_a=map(int,raw_input().split())
    chain=map(int,raw_input().split())
    M=[0]*o_a[0]
    for i in range(o_a[1]):
        M[chain[i]-1]+=1
    sums=0
    #print M
    for i in range(1,o_a[0]):
        sums+=M[i]
    #print "sums "+str(sums)
    while M[0]!=0:
        M[0]-=1
        if sums==0:
            if M[0]>=2:
                ctr+=1
                M[0]-=2
                sums+=1
            elif M[0]==1:
                ctr+=1
                break
            else :
                break
        elif sums==1 and M[0]>0:
            
            M[0]-=1
            ctr+=1
        elif sums==1 and M[0]==0:
            ctr+=1
            break
                    
    if M[0]==0:
        while sums>2:
            ctr+=2
            sums-=2
        if sums==2:
            ctr+=1
    
    print ctr
    
    #print M
    #print mat
    
    test-=1
    
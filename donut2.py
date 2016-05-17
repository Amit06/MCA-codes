'''
    @author:ph0enix
'''
import sys
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
    if sums==0 :
        ctr= M[0]//2
        
    elif sums-1==M[0] or sums <=M[0]:
        ctr=(M[0]+sums)//2
        
    elif M[0]==0:
        ctr=sums-1
    
    elif sums > M[0]:
        print o_a[1]
        ctr=o_a[1]-M[0]-1
    
    print ctr
    
    #print M
    #print mat
    
    test-=1
    
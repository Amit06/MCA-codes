def countInv(a):
    print a
    if len(a)>1:
        q=len(a)//2
        L=a[:q]
        R=a[q:]
        x=countInv(L)
        y=countInv(R)
        z=countSplitInv(a,L,R)
        return x+y+z
    else:
        return 0
        
def countSplitInv(a,L,R):
    i=0
    j=0
    k=0
    count=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
            count+=len(L)-i
        
            
        k+=1
    
    print a 
    return count
        
        
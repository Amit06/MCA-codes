def msort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        msort(L)
        msort(R) 
        merge(a,L,R)
        
def merge(a,L,R):
    i=0
    j=0
    k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1  
        k+=1
    while i<len(L):
        a[k]=L[i]
        k+=1
        i+=1
    while j<len(R):
        a[k]=R[j]
        k+=1
        j+=1  


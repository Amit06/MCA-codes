import math
best= [None,None]

def d(a,b):
    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    
def mSort(a,Q):
    
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        mSort(L,Q)
        mSort(R,Q) 
        merge(a,L,R,Q)
        
def merge(a,L,R,Q):
    i=0
    j=0
    k=0
    while i<len(L) and j<len(R):
        if L[i][Q]<R[j][Q]:
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
    
def closestPair(S):
    
    Sx=S[:]
    Py=S[:]
    mSort(Sx,0)
    mSort(Py,1)
    
    i,j=findClosestPair(Sx,Py)
    print i,j

def findClosestPair(Px,Py):
    global best
    if len(Px)==3:
        if d(Px[0],Px[1])<d(Px[0],Px[2]) and d(Px[0],Px[1])<d(Px[1],Px[2]):
            return d(Px[0],Px[1]),Px[:2]
        elif d(Px[1],Px[2])<d(Px[0],Px[2]) and d(Px[1],Px[2])<d(Px[1],Px[0]):
            return d(Px[1],Px[2]),[Px[1],Px[2]]
        else:
            return d(Px[0],Px[2]),[Px[0],Px[2]]
        
    elif len(Px)==2:
        return d(Px[0],Px[1]),Px
    else :
        xbar=Px[len(Px)//2]
        Sy=[]
        d1,p1=findClosestPair(Px[:len(Px)//2],Py)
        d2,p2=findClosestPair(Px[len(Px)//2:],Py)
        if d1<d2 and (best[0]==None or d1<best[0]):
            best=[d1,p1] 
            
        elif d2<d1 and (best[0]==None or d2<best[0]):
            best=[d2,p2]
            
        print "r",xbar[0]-best[0],xbar[0]+best[0]
        for i in range(len(Py)):
            if Py[i][0]>xbar[0]-best[0] and Py[i][0]<xbar[0]+best[0]:
                Sy.append(Py[i])
        print Sy
        for i in range(len(Sy)-1):
            for j in range(1,min(8,len(Sy)-i-1)):
                p=Sy[i]
                q=Sy[i+j]
                
                if d(p,q)<best[0]:
                    print p,q,i,j,len(Sy)
                    best[0]=d(p,q)
                    best[1]=[p,q]
        return best[0],best[1]
                
            
        
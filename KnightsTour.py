" Knights Tour "

kr,kc=map(int,raw_input().split())
if kr>=8 or kr<0 or kc>=8 or kc<0:
    print "Enter values in range 0-7"
    exit(0)

board=[[0]*8 for i in range(8)]
board[kr][kc]=1

ktmove1=[-2,-1,1,2,2,1,-1,-2]
ktmove2=[1,2,2,1,-1,-2,-2,-1]

for i in range(2,65):
    npos=0
    nexti=[]
    nextj=[]
   
    mini=-1
    for k in range(8):
        
        if kr+ktmove1[k]>=0 and kr+ktmove1[k]<8 and kc+ktmove2[k]>=0 and kc+ktmove2[k]<8 and board[kr+ktmove1[k]][kc+ktmove2[k]]==0:
            nexti.append(kr+ktmove1[k])
            nextj.append(kc+ktmove2[k])
            npos+=1
            
    exitl=[0]*npos        
    if npos==0:
        print "FAILURE @"+str(i)
        for b in board:
            print b
        break    
    if npos==1:
        mini=0
        
    
    else:
        for n in range(npos):
            for e in range(7):
                
                if nexti[n]+ktmove1[e]>=0 and nexti[n]+ktmove1[e]<8 and nextj[n]+ktmove2[e]>=0 and nextj[n]+ktmove2[e]<8 and board[nexti[n]+ktmove1[e]][nextj[n]+ktmove2[e]]==0:
                    exitl[n]+=1
        
        mini=exitl.index(min(exitl))
        
   
    kr=nexti[mini]
    kc=nextj[mini]
    board[kr][kc]=i
if i==64:        
    for b in board:
        print b

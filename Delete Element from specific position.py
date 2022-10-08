L=list(input('enter a list'))
tL=[0 for i in range(len(L)-1)]
p=input('enter the position') - 1
if p!=0:
    for i in range(p): 
        tL[i]=L[i]
for i in range(p,len(L)-1): 
    tL[i]=L[i+1]
L=tL
print L
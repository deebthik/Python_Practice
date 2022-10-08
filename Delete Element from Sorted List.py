L = list(input("Enter list : "))
x=input('enter the element to be deleted') 
p=-1
for i in range(len( L)):
    if L[i]>=x: 
        p=i
        break
        
if p!=-1:
    tL=[0 for i in range(len(L)-1)] 
    if p!=0:
        for i in range(p): 
            tL[i]=L[i]
    for i in range(p,len(L)-1): 
        tL[i]=L[i+1]
    L=tL
    print L
else:
    print 'Element not found'
L=list(input('enter a list')) 
L=L+[0]
x=input('enter the element')
p=len(L)-1
for i in range(len( L)):
    if L[i]>=x: 
        p=i
        break
for i in range(len(L)-2,p-1,-1):
    L[i+1]=L[i] 
L[p]=x
print L

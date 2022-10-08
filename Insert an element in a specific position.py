L=list(input('enter a list')) 
L=L+[0]
x=input('enter the element') 
p=input('enter the position')-1 
for i in range(len(L)-2,p-1,-1):
    L[i+1]=L[i] 

L[p]=x
print L
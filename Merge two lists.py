def Selection_Sort(L):
    for i in range(len(L)-1):
        s=L[i]
        p=i
        for j in range(i+1,len(L)):
            if(L[j]<s): 
                s=L[j]
                p=j 
        L[i],L[p]=L[p],L[i]
    return L

l1=list(input('enter a list 1 :'))
Selection_Sort(l1)
l2=list(input('enter a list 2 :'))
Selection_Sort(l2)
print 'list 1',l1,'list 2',l2
l3=[0 for i in range(len(l1)+len(l2))] # Not required id append() is used
i=0
j=0
k=0
while(i<len(l1) and j<len(l2)): 
    if l1[i]<=l2[j]:
        l3[k]=l1[i]
        i=i+1 
    else:
        l3[k]=l2[j]
        j=j+1 
    k=k+1
    
if i>=len(l1):
    while j<len(l2):
        l3[k]=l2[j] 
        j=j+1 
        k=k+1
        
elif j>=len(l2): 
    while i<len(l1):
        l3[k]=l1[i] 
        i=i+1 
        k=k+1

print 'list 3 after merging ',l3
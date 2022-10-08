L=list(input('enter a list')) 
print 'Unsorted List :',L 
for i in range(len(L)-1):
    s=L[i]
    p=i
    for j in range(i+1,len(L)):
        if(L[j]<s): 
            s=L[j]
            p=j 
    L[i],L[p]=L[p],L[i]

print 'Sorted List :',L